import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.Headers;
import com.sun.net.httpserver.HttpHandler;

import java.io.*;
import java.net.InetSocketAddress;
import java.util.UUID;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;

@SuppressWarnings("unused")
public class FakeProductPublisher {

    public static void main(String[] args) throws IOException {
        int port = 8080;
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/publish", new ProductHandler());
        server.setExecutor(null); // default executor
        System.out.println("Server running at http://localhost:" + port + "/publish");
        server.start();
    }

    static class ProductHandler implements HttpHandler {
        public void handle(HttpExchange exchange) throws IOException {
            if ("POST".equalsIgnoreCase(exchange.getRequestMethod())) {
                StringBuilder requestBody = new StringBuilder();
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(exchange.getRequestBody()))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        requestBody.append(line).append("\n");
                    }
                }

                System.out.println("Received Product Data:");
                System.out.println(requestBody);

                Gson gson = new Gson();
                JsonObject jsonInput;
                try {
                    jsonInput = gson.fromJson(requestBody.toString(), JsonObject.class);
                } catch (Exception e) {
                    System.err.println("Failed to parse JSON");
                    e.printStackTrace();
                    exchange.sendResponseHeaders(400, -1); // Bad Request
                    return;
                }

                // ✅ Create JSON response with original product data
                JsonObject jsonResponse = new JsonObject();
                jsonResponse.addProperty("status", "success");
                jsonResponse.addProperty("product_id", "fake-" + UUID.randomUUID().toString().substring(0, 6));
                jsonResponse.add("product_data", jsonInput);  // <- include full product data here

                byte[] responseBytes = gson.toJson(jsonResponse).getBytes();

                Headers headers = exchange.getResponseHeaders();
                headers.add("Content-Type", "application/json");

                exchange.sendResponseHeaders(200, responseBytes.length);
                try (OutputStream os = exchange.getResponseBody()) {
                    os.write(responseBytes);
                }
            } else {
                exchange.sendResponseHeaders(405, -1); // Method Not Allowed
            }
        }
    }
}


// to compile - javac -cp gson-2.10.1.jar -d . FakeProductPublisher.java
// to run - java -cp ".;gson-2.10.1.jar" FakeProductPublisher