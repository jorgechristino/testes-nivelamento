<template>
  <div class="container">
    <h1>Adicionar Nova Operadora</h1>
    <form @submit.prevent="createOperadora">  
      <label for="registro_ans">Registro ANS</label>
      <input v-model="operadora.registro_ans" type="text" id="registro_ans" required />
    
      <label for="cnpj">CNPJ</label>
      <input v-model="operadora.cnpj" type="text" id="cnpj" required />
    
      <label for="razao_social">Razão Social</label>
      <input v-model="operadora.razao_social" type="text" id="razao_social" required />
    
      <label for="nome_fantasia">Nome Fantasia</label>
      <input v-model="operadora.nome_fantasia" type="text" id="nome_fantasia" />
    
      <label for="modalidade">Modalidade</label>
      <input v-model="operadora.modalidade" type="text" id="modalidade" />
    
      <label for="logradouro">Logradouro</label>
      <input v-model="operadora.logradouro" type="text" id="logradouro" />
    
      <label for="numero">Número</label>
      <input v-model="operadora.numero" type="text" id="numero" />
    
      <label for="complemento">Complemento</label>
      <input v-model="operadora.complemento" type="text" id="complemento" />
    
      <label for="bairro">Bairro</label>
      <input v-model="operadora.bairro" type="text" id="bairro" />
    
      <label for="cidade">Cidade</label>
      <input v-model="operadora.cidade" type="text" id="cidade" />
    
      <label for="uf">UF</label>
      <input v-model="operadora.uf" type="text" id="uf" required />
    
      <label for="cep">CEP</label>
      <input v-model="operadora.cep" type="text" id="cep" />
    
      <label for="ddd">DDD</label>
      <input v-model="operadora.ddd" type="text" id="ddd" />
    
      <label for="telefone">Telefone</label>
      <input v-model="operadora.telefone" type="text" id="telefone" />
  
      <label for="fax">Fax</label>
      <input v-model="operadora.fax" type="text" id="fax" />
    
      <label for="endereco_eletronico">Endereço Eletrônico</label>
      <input v-model="operadora.endereco_eletronico" type="email" id="endereco_eletronico" />
    
      <label for="representante">Representante</label>
      <input v-model="operadora.representante" type="text" id="representante" />
    
      <label for="cargo_representante">Cargo do Representante</label>
      <input v-model="operadora.cargo_representante" type="text" id="cargo_representante" />
    
      <label for="regiao_de_comercializacao">Região de Comercialização</label>
      <input v-model="operadora.regiao_de_comercializacao" type="number" id="regiao_de_comercializacao"  required/>
    
      <label for="data_registro_ans">Data Registro ANS</label>
      <input v-model="operadora.data_registro_ans" type="date" id="data_registro_ans" required />
    
      <button type="submit" class="btn">Adicionar Operadora</button>
    </form>
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
  data() {
    return {
      operadora: {
        registro_ans: '',
        cnpj: '',
        razao_social: '',
        nome_fantasia: '',
        modalidade: '',
        logradouro: '',
        numero: '',
        complemento: '',
        bairro: '',
        cidade: '',
        uf: '',
        cep: '',
        ddd: '',
        telefone: '',
        fax: '',
        endereco_eletronico: '',
        representante: '',
        cargo_representante: '',
        regiao_de_comercializacao: '',
        data_registro_ans: ''
      },
    };
  },
  methods: {
    async createOperadora() {
      try {
        const response = await axios.post("http://localhost:8000/api/v1/operadoras/", this.operadora);
        this.toast.success("Operadora criada com sucesso!", { position: "top-right" });
        this.clearForm();
      } catch (error) {
        console.error("Erro ao criar operadora:", error);
        this.toast.error("Erro ao criar operadora!", { position: "top-right" });
      }
    },
    clearForm() {
      this.operadora = {
        registro_ans: '',
        cnpj: '',
        razao_social: '',
        nome_fantasia: '',
        modalidade: '',
        logradouro: '',
        numero: '',
        complemento: '',
        bairro: '',
        cidade: '',
        uf: '',
        cep: '',
        ddd: '',
        telefone: '',
        fax: '',
        endereco_eletronico: '',
        representante: '',
        cargo_representante: '',
        regiao_de_comercializacao: '',
        data_registro_ans: ''
      };
    },
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

input {
  border: 1px solid #eee;
  display: block;
  width: 100%;
  font-size: 1rem;
  padding: 13px;
  border-radius: 6px;
  background: #eee;
  transition: 0.1s;
  margin-bottom: 16px;
}

input:focus,
input:hover {
  outline: none;
  border-color: #9D4EF1;
  background: white;
  box-shadow: 0 0 0 3px #bd90ee;
}

label {
  display: block;
  font-size: 15px;
  line-height: 1;
  padding-bottom: 8px;
  font-weight: 600;
}

.btn {
  padding: 13px 18px;
  margin: 5px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  background-color: #28a745;
  color: white;
}

</style>
