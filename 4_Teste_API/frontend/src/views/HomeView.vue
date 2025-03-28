<template>
  <div class="container">
    <h1>Lista de Operadoras de Planos de Saúde</h1>
    <OperadorasTable
      v-if="operadoras.length" 
      :operadoras="operadoras"
      :reloadOperadoras="fetchOperadoras"
    />
    
  </div>
</template>

<script>
import OperadorasTable from '@/components/OperadorasTable.vue';
import axios from 'axios';

export default {
  components: { OperadorasTable },
  data() {
    return {
      operadoras: [],
    };
  },
  methods: {
    async fetchOperadoras() {
      try {
        const response = await axios.get("http://localhost:8000/api/v1/operadoras/");
        this.operadoras = response.data;
      } catch (error) {
        console.error("Erro ao listar operadoras:", error);
      }
    },
  },
  mounted() {
    this.fetchOperadoras();
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

</style>
