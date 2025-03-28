<template>
      <table class="operadoras-table">
      <thead>
        <tr>
          <th>Registro ANS</th>
          <th>Razão Social</th>
          <th>Nome Fantasia</th>
          <th>Modalidade</th>
          <th>UF</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="operadora in paginatedOperadoras" :key="operadora.registro_ans">
          <td>{{ operadora.registro_ans }}</td>
          <td>{{ operadora.razao_social }}</td>
          <td>{{ operadora.nome_fantasia }}</td>
          <td>{{ operadora.modalidade }}</td>
          <td>{{ operadora.uf }}</td>
          <td class="actions">
            <button class="edit-btn" @click="openModal(operadora)">
              <img src="../assets/icons/edit.svg" alt="edit icon">
            </button>
            <button class="delete-btn" @click="deleteOperadora(operadora.id)">
              <img src="../assets/icons/delete.svg" alt="delete icon">
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Paginação -->
    <div class="pagination">
      <button @click="previousPage" :disabled="currentPage === 1">❮</button>
      <span>Página {{ currentPage }} de {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">❯</button>
    </div>

    <!-- Modal de Edição -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2>Editar Operadora</h2>
        <label>Razão Social</label>
        <input v-model="operadoraEdit.razao_social" type="text" />

        <label>Nome Fantasia</label>
        <input v-model="operadoraEdit.nome_fantasia" type="text" />

        <label>Modalidade</label>
        <input v-model="operadoraEdit.modalidade" type="text" />

        <label>UF</label>
        <input v-model="operadoraEdit.uf" type="text" />

        <div class="modal-actions">
          <button @click="updateOperadora">Salvar</button>
          <button @click="showModal = false">Cancelar</button>
        </div>
      </div>
    </div>
</template>


<script>
import axios from 'axios';
import {useToast} from 'vue-toast-notification';

export default {
  setup() {
    const toast = useToast();
    return { toast };
  },
  props: ['operadoras', 'reloadOperadoras'],
  data() {
    return {
      currentPage: 1,
      perPage: 10, // Número de itens por página
      showModal: false,
      operadoraEdit: {
        id: null,
        razao_social: "",
        nome_fantasia: "",
        modalidade: "",
        uf: ""
      }
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.operadoras.length / this.perPage);
    },
    paginatedOperadoras() {
      const start = (this.currentPage - 1) * this.perPage;
      return this.operadoras.slice(start, start + this.perPage);
    }
  },
  methods: {
    openModal(operadora) {
      this.operadoraEdit = { ...operadora };
      this.showModal = true;
    },
    async updateOperadora() {
      try {
        await axios.put(`http://localhost:8000/api/v1/operadoras/${this.operadoraEdit.id}`, this.operadoraEdit);
        this.toast.success("Operadora atualizada com sucesso!", { position: "top-right" });
        this.reloadOperadoras();
        this.showModal = false;
      } catch (error) {
        this.toast.error("Erro ao editar operadora!", { position: "top-right" });
        console.error("Erro ao editar operadora:", error);
      }
    },
    async deleteOperadora(id) {
      if (confirm("Tem certeza que deseja excluir esta operadora?")) {
        try {
          await axios.delete(`http://localhost:8000/api/v1/operadoras/${id}`);
          this.toast.success("Operadora excluída com sucesso!", { position: "top-right" });
          this.reloadOperadoras();
        } catch (error) {
          this.toast.error("Erro ao excluir operadora!", { position: "top-right" });
          console.error("Erro ao excluir operadora:", error);
        }
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    }
  },
};
</script>

<style scoped>

/* Estilo da tabela */
.operadoras-table {
  width: 100%;
  border-collapse: collapse;
  background: white;
}

.operadoras-table th, .operadoras-table td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}

.operadoras-table th {
  background-color: #9D4EF1;
  color: white;
}

.operadoras-table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.actions{
  display: flex;
  align-items: center;
  gap: 10px; 
  height: 80px;
}

.edit-btn, .delete-btn {
  padding: 7px;
  width: 40px;
  height: 40px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.edit-btn img, .delete-btn img{
  width: 100%;
}

.edit-btn {
  background-color: #ffc107;
}

.delete-btn {
  background-color: #dc3545;
}

.pagination {
  margin-top: 20px;
}

.pagination button {
  padding: 8px 12px;
  margin: 0 5px;
  border: none;
  cursor: pointer;
  background-color: #9D4EF1;
  color: white;
  border-radius: 5px;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

/* Estilo do modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 600px;
}

.modal-content input {
  border: 1px solid #f2f2f2;
  display: block;
  width: 100%;
  font-size: 1rem;
  padding: 13px;
  border-radius: 6px;
  background: #f2f2f2;
  transition: 0.1s;
  margin-bottom: 16px;
}

.modal-content input:focus,
.modal-content input:hover {
  outline: none;
  border-color: #9D4EF1;
  background: white;
  box-shadow: 0 0 0 3px #bd90ee;
}

.modal-content label {
  display: block;
  font-size: 15px;
  line-height: 1;
  padding-bottom: 8px;
  font-weight: 600;
}

.modal-actions {
  margin-top: 10px;
}

.modal-actions button {
  padding: 13px 18px;
  margin: 5px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.modal-actions button:first-child {
  background-color: #28a745;
  color: white;
}

.modal-actions button:last-child {
  background-color: #dc3545;
  color: white;
}
</style>