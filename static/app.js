document.addEventListener("click", async (event) => {
  const button = event.target.closest("[data-copy]");
  if (!button) return;
  const value = button.dataset.copy;
  const status = document.getElementById("copy-status");
  try {
    await navigator.clipboard.writeText(value);
    if (status) status.textContent = "Server address copied!";
    button.textContent = "Copied!";
  } catch {
    if (status) status.textContent = "Copy unavailable. Select the address and copy it manually.";
  }
});
