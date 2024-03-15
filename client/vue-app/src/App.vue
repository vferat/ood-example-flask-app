<script>
import FmriprepForm from './components/FmriprepForm.vue';

const apiEndpoint = '/pun/dev/ood-example-flask-app/api_v1/';

export default {
  name: 'App',
  components: {
    FmriprepForm
  },
  data() {
    return {
      name: 'test',
      showModal: false,
      alert: null
    }
  },

  mounted() {
      this.fetchData();
  },

  methods: {
    fetchData() {
      console.log('fetching data');
      fetch(apiEndpoint + 'greeting')
          .then(response => response.json())
          .then(data => {
              this.name = data.name;
          })
          .catch(error => {
              console.error('Error fetching data:', error);
          });
    },
    toggleModal() {
      this.showModal = !this.showModal;
      console.log('showModal:', this.showModal);
    },
    showAlert() {
      console.log('showAlert');
      this.alert = 1;
      setTimeout(this.hideAlert, 10000);
    },
    hideAlert() {
      this.alert = null;
    }
  }
}
</script>

<template>

<main role="main">

  <div v-if = "showModal">
    <FmriprepForm @message="showAlert" @close="toggleModal"/>
  </div>

  <div v-if="alert" :style="{ backgroundColor: alert.type === 'error' ? 'red' : alert.type === 'warning' ? 'yellow' : 'green', padding: '10px' }">
    {{ alert.message }}
  </div>

  <section class="jumbotron text-center">
    <div class="container">
      <h1>Applications</h1>
      <p class="lead text-muted">
        A collection of Apptainer applications that can be run on UNGIE's HPC.
      </p>
    </div>
  </section>



  <div class="album py-5 bg-light">
    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <div class="card mb-4 shadow-sm">
            <svg
              class="bd-placeholder-img card-img-top"
              width="100%"
              height="225"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="xMidYMid slice"
              focusable="false"
              role="img"
              aria-label="Placeholder: Thumbnail"
            >
              <title>Placeholder</title>
              <rect width="100%" height="100%" fill="#55595c"></rect>
              <text x="50%" y="50%" fill="#eceeef" dy=".3em">
                FMRIPREP
              </text>
            </svg>
            <div class="card-body">
              <p class="card-text">
                fMRIPrep is a functional magnetic resonance imaging (fMRI) data preprocessing pipeline.
              </p>
              <div
                class="d-flex justify-content-between align-items-center"
              >
                <div class="btn-group">
                  <button @click="toggleModal"
                    type="button"
                    class="btn btn-sm btn-outline-secondary"
                  >
                    Run
                  </button>
                </div>
                <small class="text-muted">vO.O.1</small>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card mb-4 shadow-sm">
            <svg
              class="bd-placeholder-img card-img-top"
              width="100%"
              height="225"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="xMidYMid slice"
              focusable="false"
              role="img"
              aria-label="Placeholder: Thumbnail"
            >
              <title>Placeholder</title>
              <rect width="100%" height="100%" fill="#55595c"></rect>
              <text x="50%" y="50%" fill="#eceeef" dy=".3em">
                MRIQC
              </text>
            </svg>
            <div class="card-body">
              <p class="card-text">
                MRIQC extracts no-reference IQMs (image quality metrics) 
                from structural (T1w and T2w) and functional MRI 
                (magnetic resonance imaging) data.
              </p>
              <div
                class="d-flex justify-content-between align-items-center"
              >
                <div class="btn-group">
                  <button
                    type="button"
                    class="btn btn-sm btn-outline-secondary"
                  >
                    Run
                  </button>
                </div>
                <small class="text-muted">v1.2.3</small>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</main>

</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  border-bottom: 1px solid #ddd;
  display: inline-block;
  padding-bottom: 10px;
}
</style>
