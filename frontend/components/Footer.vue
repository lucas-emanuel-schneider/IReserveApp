<template>
  <footer class="footer-container">
    <div class="footer-content">
      <div class="footer-contact">
        <p>Telefone: (+503) 1234-5678</p>
        <p>Email: <span class="footer-email">IReserve@reserv.com</span></p>
        <p>Site: <span class="footer-site">www.IReserve.com</span></p>
      </div>
      <address class="footer-address">
        123 rd, Sc - 00000
      </address>
    </div>
  </footer>
</template>

<script>
export default {};
</script>

<style>

.footer-container {
  color: #fff;
  padding: 20px;
  text-align: center;
  font-family: Arial, sans-serif;
}

.footer-content {
  display: flex;
  color: #282c34;
  flex-direction: column;
  align-items: center;
}

.footer-contact p {
  margin: 5px 0;
}

.footer-email {
  font-weight: bold;
  color: #007bff;
  cursor: pointer;
}

.footer-site {
  font-weight: bold;
  color: #007bff;
  cursor: pointer;
}

.footer-address {
  margin-top: 15px;
}
</style>
