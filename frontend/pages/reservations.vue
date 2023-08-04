<template>
  <div>
    <NavBar />
    <NuxtChild />
  </div>
</template>

<script>
export default {
    head() {
      return { title: 'Reservas',
      meta: [
        { hid: 'description', name: 'description', content: 'Minhas Reservas' },
      ]}
    },
    middleware: 'auth',

}
</script>

<style>

</style>