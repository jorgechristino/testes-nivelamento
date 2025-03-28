<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/adicionar">Adicionar Operadora</router-link>
      <router-link to="/buscar">Buscar Operadora</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style scoped>
nav{
  max-width: 1024px;
  display: flex;
  gap: 30px;
  margin: 0 auto;
}

nav a {
  color: #9D4EF1;
  text-decoration: none;
  padding: 20px;
  font-size: 18px;
  position: relative;
}

nav a::after{
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0px;
  height: 2px;
  background-color: #9D4EF1;
  transition: 0.3s;
}

nav a:hover:after{
  width: 100%;
}

</style>