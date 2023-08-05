<template>
  <div class="home">
    <Welcome />
    <Login />
    <Footer />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'Home',
})
</script>
<style scoped>
.home {
  margin: 20px;
  padding: 10px;
}
</style>
