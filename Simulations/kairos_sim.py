import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# --- CONFIGURATION K.A.I.R.O.S ---
N = 100              # Nombre d'oscillateurs (horloges)
K = 2.0              # Force de couplage (La "tension" du moment présent)
TIME_STEPS = 1000    # Durée de la simulation
DT = 0.05            # Pas de temps

# --- MODÉLISATION DE LA GRAVITÉ ---
# On simule une ligne d'horloges s'approchant d'une masse.
# Les horloges proches (index 0) sont "lentes" (dilatation temporelle forte).
# Les horloges lointaines (index N) sont "rapides" (temps plat).
# Ceci crée le gradient de fréquence (désaccord) mentionné dans le rapport.
radii = np.linspace(2, 10, N)  # Distance arbitraire du trou noir (Rayon Schwarzschild = 1)
natural_frequencies = 1.0 * np.sqrt(1 - 1.0/radii) # Formule RG simplifiée: omega = w0 * sqrt(1 - rs/r)

# --- MODÈLE DE KURAMOTO ---
def kuramoto_model(theta, t, omega, K, n):
    dtheta = np.zeros(n)
    # Pour chaque oscillateur i
    for i in range(n):
        # Somme des interactions avec les autres (Couplage sinus)
        interaction = 0
        for j in range(n):
            interaction += np.sin(theta[j] - theta[i])
        
        # Équation: Vitesse = Fréquence Propre (Gravité) + Couplage / N
        dtheta[i] = omega[i] + (K / n) * interaction
    return dtheta

# --- INITIALISATION ---
# Phases aléatoires au début (pas de "présent" défini)
initial_phases = np.random.uniform(0, 2*np.pi, N)
t = np.linspace(0, TIME_STEPS*DT, TIME_STEPS)

# --- RÉSOLUTION ---
print(f"Lancement de la simulation KAIROS avec K={K}...")
theta_solution = odeint(kuramoto_model, initial_phases, t, args=(natural_frequencies, K, N))

# --- CALCUL DU PARAMÈTRE D'ORDRE (COHÉRENCE) ---
# r(t) mesure à quel point le "présent" est solide (0 = chaos, 1 = synchronisation parfaite)
order_param = np.abs(np.mean(np.exp(1j * theta_solution), axis=1))

# --- VISUALISATION ---
plt.figure(figsize=(12, 6))

# Plot 1: Le "Présent" au cours du temps
plt.subplot(1, 2, 1)
plt.plot(t, order_param, color='purple', linewidth=2)
plt.title(f'Solidité du "Moment Présent" (K={K})')
plt.xlabel('Temps Système')
plt.ylabel('Cohérence (r)')
plt.ylim(0, 1.1)
plt.grid(True, alpha=0.3)

# Plot 2: Fréquences effectives (La Cascade)
# On regarde si les horloges ont réussi à se synchroniser malgré la gravité
effective_frequencies = np.diff(theta_solution, axis=0) / DT
avg_freq = np.mean(effective_frequencies[int(TIME_STEPS/2):], axis=0)

plt.subplot(1, 2, 2)
plt.plot(radii, natural_frequencies, 'k--', label='Temps Gravitationnel (RG)')
plt.plot(radii, avg_freq, 'r-', label='Temps Émergent (KAIROS)')
plt.title('La Cascade de Désynchronisation')
plt.xlabel('Distance au Trou Noir')
plt.ylabel('Vitesse d\'écoulement du temps')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Simulation terminée. Si la ligne rouge suit la ligne noire, la gravité a gagné (pas de présent unique).")
print("Si la ligne rouge est plate, le couplage a gagné (Présent synchronisé).")
---
