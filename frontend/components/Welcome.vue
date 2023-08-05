<template>
    <div class="welcome-container">
      <h1>Bem-vindo(a) a página de reservas IReserve!</h1>
      <p class="welcome-text">Aqui você pode efetuar as suas reservas nos espaços físicos da empresa.</p>
    </div>
</template>

<script>
export default {};
</script>

<style>
.welcome-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-bottom: 20px;
}

h1 {
  font-size: 3rem;
  color: #333;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
  margin: 0;
  padding: 20px;
  border: 4px solid #3498db;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.welcome-text {
  font-size: 1.5rem;
  color: #444;
  margin-top: 10px;
  text-align: center;
  line-height: 1.5;
}
</style>
