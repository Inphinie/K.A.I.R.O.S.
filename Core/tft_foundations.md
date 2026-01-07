# Fondements Mathématiques : Théorie du Champ Temporel (TFT)

## 1. Le Lagrangien du Champ Temporel
Selon la TFT, le temps est traité non comme une coordonnée, mais comme un champ scalaire réel dynamique $\mathcal{T}(x^\mu)$. L'action est définie par :

$$S = \int d^4x \sqrt{-g} (\mathcal{L}_T + \mathcal{L}_{int})$$

### Lagrangien Libre ($\mathcal{L}_T$)
$$\mathcal{L}_T = \frac{1}{2} g^{\mu\nu} \partial_\mu \mathcal{T} \partial_\nu \mathcal{T} - V(\mathcal{T})$$

### Terme d'Interaction ($\mathcal{L}_{int}$)
Le couplage est sourcé par la densité de flux d'entropie et d'information :
$$\mathcal{L}_{int} = - \mathcal{T} \rho_t$$
Où la densité source $\rho_t$ est :
$$\rho_t = \alpha \nabla_\mu s^\mu + \beta \nabla_\mu I^\mu$$

## 2. Chronotension et Chronocourbure
Ces quantités définissent la "rigidité" du présent émergent.

* **Chronotension ($\tau$) :** Le gradient du champ temporel.
    $$\tau = \nabla \mathcal{T}$$
    Représente la force de synchronisation locale.

* **Chronocourbure ($K_{\mathcal{T}}$) :** Le Laplacien du champ.
    $$K_{\mathcal{T}} = \nabla^2 \mathcal{T}$$

## 3. Équation du Mouvement Relativiste Couplée (KAIROS)
L'évolution de la phase $\theta$ (temps local) est une compétition entre la métrique (RG) et le couplage (Kuramoto) :

$$\frac{d\theta}{dt} = \omega_0 \sqrt{g_{00}(x)} + K(x,t) \int \sin(\theta(y) - \theta(x)) d^3y$$

Le "Présent" global émerge si le terme de droite (Couplage) domine le terme de gauche (Dilatation).
