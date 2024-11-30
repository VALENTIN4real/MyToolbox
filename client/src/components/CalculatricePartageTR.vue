<template>
  <div class="container">
    <h1>Calculatrice de partage de TR</h1>
      <div class="mb-3">
        <label for="Montant de la commande" class="form-label">Montant de la commande</label>
        <input v-model="montantCommande" type="number" step="0.01" class="form-control" id="montantCommande" aria-describedby="Montant de la commande">
      </div>
      <div class="mb-3">
        <label for="Montant titre-restaurants utilisés" class="form-label">Montant titre-restaurants utilisés</label>
        <input v-model="montantTRUtilises" type="number" step="0.01" class="form-control" id="montantTRUtilises">
      </div>
      <div class="mb-3">
        <label for="Part salariale d'un titre-restaurant" class="form-label">Part salariale d'un titre-restaurant</label>
        <input v-model="partSalarialeTR" type="number" step="0.01" class="form-control" id="partSalariale">
      </div>
      <div class="mb-3">
        <label for="Part patronale d'un titre-restaurant" class="form-label">Part patronale d'un titre-restaurant</label>
        <input v-model="partPatronaleTR" type="number" step="0.01" class="form-control" id="partPatronale">
      </div>
      <button class="btn btn-primary" @click="calcul">Calculer</button>

    <div class="mt-3">
      <p>Montant hors titre-restaurants : {{ montantHorsTR }}€</p>
      <p>Total TR salarial : {{ totalCoutTRSalarial }}€</p>
      <p>Total TR patronal : {{ totalCoutTRPatronal }}€</p>
      <p>Coût total de la commande : {{ totalCoutCommande }}€</p>
      <p>Coût total de la commande, part patronale déduite : {{ totalCoutCommandeAvecPatronalDeduit }}€</p>
      <p>Coût total de la commande sans TR divisé par 2 : {{ totalCoutCommandeSansTRPartage }}€</p>
      <p>Coût Val hors TR : {{ coutVal }}€</p>
      <p>Coût Réel Val : {{ coutReelVal }}€</p>
      <p>Coût Gwén : {{ coutGwen }}€</p>
      <p>Coût Réel Gwén : {{ coutReelGwen }}€</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CalculatricePartageTR',
  data() {
    return {
      montantCommande: 33.92,
      montantTRUtilises: 25,
      partSalarialeTR: 4.61,
      partPatronaleTR: 6.91,
      valeurTitre: 11.52,
      montantHorsTR: 0,
      totalCoutTRSalarial: 0,
      totalCoutTRPatronal: 0,
      totalCoutCommande: 0,
      totalCoutCommandeAvecPatronalDeduit: 0,
      totalCoutCommandeSansTRPartage: 0,
      pourcentagePartSalarialeTR: 0,
      coutVal: 0,
      coutGwen: 0,
      coutReelGwen: 0,
      coutReelVal: 0

    };
  },

  methods: {
    calcul() {
      // Calculer le montant hors TR
      this.montantHorsTR = this.montantCommande - this.montantTRUtilises;

      // Calculer le total du coût TR salarial
      this.totalCoutTRSalarial = this.montantTRUtilises * this.partSalarialeTR / this.valeurTitre;

      // Calculer le total du coût TR patronal
      this.totalCoutTRPatronal = this.montantTRUtilises * this.partPatronaleTR / this.valeurTitre;

      // Calculer le total du coût de la commande
      this.totalCoutCommande = this.montantCommande;

      this.totalCoutCommandeAvecPatronalDeduit = this.totalCoutCommande - this.totalCoutTRPatronal;

      // Calculer le coût sans TR (partage entre Valentin et Gwén)
      this.totalCoutCommandeSansTRPartage = this.totalCoutCommandeAvecPatronalDeduit / 2;

      // Calculer la part salariale de Valentin (ce qu'il paye réellement)
      this.coutVal = this.totalCoutCommandeSansTRPartage - this.totalCoutTRSalarial;

      // Gwén doit simplement payer la part salariale de Valentin, sans tenir compte de la part patronale
      this.coutGwen = this.totalCoutCommandeSansTRPartage;

      // Calculer le coût réel pour Valentin (s'il a payé plus que ce qu'il aurait dû)
      this.coutReelVal = this.coutVal + this.totalCoutTRSalarial;

      // Si Valentin a payé plus de TR que ce qu'il aurait dû, alors Gwén lui doit de l'argent
      if (this.coutVal < 0) {
        this.coutReelGwen = this.coutGwen + Math.abs(this.coutVal);
      } else {
        this.coutReelGwen = this.coutGwen;
      }

      // Tout arrondir
      this.montantHorsTR = Math.round(this.montantHorsTR * 100) / 100;
      this.totalCoutTRSalarial = Math.round(this.totalCoutTRSalarial * 100) / 100;
      this.totalCoutTRPatronal = Math.round(this.totalCoutTRPatronal * 100) / 100;
      this.totalCoutCommande = Math.round(this.totalCoutCommande * 100) / 100;
      this.totalCoutCommandeAvecPatronalDeduit = Math.round(this.totalCoutCommandeAvecPatronalDeduit * 100) / 100;
      this.totalCoutCommandeSansTRPartage = Math.round(this.totalCoutCommandeSansTRPartage * 100) / 100;
      this.coutVal = Math.round(this.coutVal * 100) / 100;
      this.coutGwen = Math.round(this.coutGwen * 100) / 100;
      this.coutReelGwen = Math.round(this.coutReelGwen * 100) / 100;
      this.coutReelVal = Math.round(this.coutReelVal * 100) / 100;
    }

  },
}
</script>

<style scoped>

</style>
