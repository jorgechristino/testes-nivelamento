<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <div class="search">
      <img class="icon" src="../assets/icons/search.svg" alt="search icon">
      <input v-model="termo" placeholder="Digite o nome da operadora..." @keyup.enter="buscarOperadoras"/>
    </div>

    <OperadorasTable
      v-if="operadoras.length" 
      :operadoras="operadoras"
      :reloadOperadoras="buscarOperadoras"
    />
    <p v-else-if="search">Nenhuma operadora encontrada.</p>
  </div>
</template>

<script>
import OperadorasTable from '@/components/OperadorasTable.vue';
import axios from 'axios';

export default {
  components: { OperadorasTable },
  data() {
    return {
      termo: '',
      operadoras: [],
      search: false
    };
  },
  methods: {
    async buscarOperadoras() {
      if (!this.termo) return;
      try {
        const response = await axios.get(`http://localhost:8000/api/v1/operadoras/search?termo=${this.termo}`);
        this.operadoras = response.data;
        this.search = true;
      } catch (error) {
        this.operadoras = [];
        console.error("Erro ao buscar operadoras:", error);
      }
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 1024px;
  margin: 30px auto;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.search {
  display: flex;
  line-height: 28px;
  align-items: center;
  position: relative;
  margin-bottom: 20px;
}

input {
  border: 1px solid #eee;
  display: block;
  width: 400px;
  font-size: 1rem;
  padding: 13px;
  border-radius: 6px;
  background: #eee;
  transition: 0.1s;
  padding-left: 48px;
}

input:focus,
input:hover {
  outline: none;
  border-color: #9D4EF1;
  background: white;
  box-shadow: 0 0 0 3px #bd90ee;
}

.icon {
  position: absolute;
  left: 16px;
  width: 20px;
  height: 20px;
}

</style>
