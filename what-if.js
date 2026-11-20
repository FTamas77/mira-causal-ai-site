// Local, assumption-based demo. No backend calls and no data collection.
(() => {
  "use strict";
  const get = (id) => document.getElementById(id);
  const flowInput = get("flowInput");
  const loadInput = get("loadInput");
  const ambientInput = get("ambientInput");
  if (!flowInput || !loadInput || !ambientInput) return;

  const evaluated = (flow, load, ambient) => ({
    flow,
    temperature: 68 + 0.15 * (load - 65) + 0.22 * (ambient - 24) - 0.20 * (flow - 50),
    energy: 85 + 0.75 * load + 0.45 * flow
  });
  const format = (n) => n.toFixed(2);
  const reset = () => {
    flowInput.value = "50";
    loadInput.value = "80";
    ambientInput.value = "29";
    render();
  };
  const render = () => {
    const flow = Number(flowInput.value);
    const load = Number(loadInput.value);
    const ambient = Number(ambientInput.value);
    const current = evaluated(flow, load, ambient);
    const choices = [35, 50, 65].map((value) => evaluated(value, load, ambient));
    const viable = choices.filter((choice) => choice.temperature <= 72);
    viable.sort((a, b) => a.energy - b.energy);
    const best = viable[0] ?? null;

    get("flowValue").textContent = flow + " L/min";
    get("loadValue").textContent = load + "%";
    get("ambientValue").textContent = ambient + "°C";
    get("simTemp").textContent = format(current.temperature) + "°C";
    get("simEnergy").textContent = format(current.energy) + " kWh";
    get("simTempBar").style.width =
      Math.max(0, Math.min(100, (current.temperature - 60) / 20 * 100)) + "%";

    const withinLimit = current.temperature <= 72;
    const verdict = get("simVerdict");
    verdict.textContent = withinLimit ? "✓ Within temperature limit" : "× Exceeds temperature limit";
    verdict.classList.toggle("sim-bad", !withinLimit);
    get("simRecommendation").textContent = best ? best.flow + " L/min" : "No feasible setting";

    choices.forEach((choice) => {
      const container = get("option" + choice.flow);
      const feasible = choice.temperature <= 72;
      container.classList.toggle("best", Boolean(best && choice.flow === best.flow));
      container.classList.toggle("not-feasible", !feasible);
      get("option" + choice.flow + "Energy").textContent = format(choice.energy) + " kWh";
      const description = !feasible
        ? "Above 72°C limit"
        : best && choice.flow === best.flow
          ? "Lowest feasible energy"
          : "Feasible";
      get("option" + choice.flow + "Temp").textContent =
        format(choice.temperature) + "°C · " + description;
    });
  };

  [flowInput, loadInput, ambientInput].forEach((input) =>
    input.addEventListener("input", render));
  get("simReset").addEventListener("click", reset);
  render();
})();
