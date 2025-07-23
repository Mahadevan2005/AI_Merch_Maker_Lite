const mockupInput = document.getElementById("mockupUpload");
const designInput = document.getElementById("designUpload");
const placementSelect = document.getElementById("placement");
const canvas = document.getElementById("designCanvas");
const ctx = canvas.getContext("2d");
const jsonOutput = document.getElementById("jsonOutput");

canvas.width = 500;
canvas.height = 600;

let mockupImage = null;
let designImage = null;
const mockupData = {};

function renderCanvas() {
  if (!mockupImage || !designImage) return;

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(mockupImage, 0, 0, canvas.width, canvas.height);

  const designWidth = 200;
  const designHeight = 200;
  const x = (canvas.width - designWidth) / 2;
  const y = 200;

  ctx.drawImage(designImage, x, y, designWidth, designHeight);

  const placement = placementSelect.value;
  const base64 = canvas.toDataURL("image/png");
  mockupData[placement] = base64;
}

mockupInput.addEventListener("change", (e) => {
  const file = e.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function (event) {
    mockupImage = new Image();
    mockupImage.onload = renderCanvas;
    mockupImage.src = event.target.result;
  };
  reader.readAsDataURL(file);
});

designInput.addEventListener("change", (e) => {
  const file = e.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function (event) {
    designImage = new Image();
    designImage.onload = renderCanvas;
    designImage.src = event.target.result;
  };
  reader.readAsDataURL(file);
});

document.getElementById("generateJson").addEventListener("click", () => {
  const mockups = Object.keys(mockupData).map((placement) => ({
    placement: placement,
    variant_ids: [4012],
    mockup_url: mockupData[placement]
  }));

  const json = {
    mockups: mockups,
    status: "success",
    created_at: new Date().toLocaleString('en-IN', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      hour12: true
    })
  };

  const jsonText = JSON.stringify(json, null, 2);
  jsonOutput.textContent = jsonText;
  document.getElementById("copyIcon").style.display = "block";
});

document.getElementById("copyIcon").addEventListener("click", () => {
  const json = document.getElementById("jsonOutput").textContent;
  navigator.clipboard.writeText(json)
    .then(() => {
      const btn = document.getElementById("copyIcon");
      btn.textContent = "Copied";
      setTimeout(() => btn.textContent = "📋", 3000);
    })
    .catch(() => alert("Copy failed"));
});


document.getElementById("downloadMockup").addEventListener("click", () => {
  const link = document.createElement("a");
  link.download = "mockup_with_design.png";
  link.href = canvas.toDataURL("image/png");
  link.click();
});