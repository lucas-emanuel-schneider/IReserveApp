<template>
<div>
  <div v-if="$fetchState.pending">
    Carregando...
  </div>
<div v-else>
  <h1>Página de reservas, onde vai ta as tuas reservas já feitas!</h1>
  <div v-for="product in products" :key="product.id">
    {{ product.title }}
  </div>
</div>
</div>
</template>

<script>
export default {
  data() {
    return {
      products: []
    };
  },
  async fetch() {
    this.products = await this.$axios.$get('https://jsonplaceholder.typicode.com/posts?_limit=5')
  }
}
</script>

<style>

</style>