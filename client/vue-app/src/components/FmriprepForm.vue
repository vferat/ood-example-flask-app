<template>
  <div class="modal-backdrop">
    <div class="modal-main">
      <h1>fMRIPrep</h1>
      <form>
        <label>BIDS dir</label>
        <input type="text" required v-model="bidsDir"/>
        <button @click="submit">Run</button>
      </form>
    </div>
  </div>
</template>

<script>

const apiEndpoint ='/pun/dev/ood-example-flask-app/api_v1/'


export default {
    data() {
        return {
            bidsDir: ''
        }
    },
    methods: {
      submit() {
          console.log('Submitting job');
          fetch(apiEndpoint + 'submit')
              .then(response => response.json())
              .then(data => {
                  console.log(data.jobs);
              })
              .catch(error => {
                  console.error('Error fetching data:', error);
              });
      }
    }
}
</script>

<style>
  .modal-main {
    width: 400px;
    padding: 20px;
    margin: 200px auto;
    background: white;
    border-radius: 10px;
  }
  .modal-backdrop {
    top: 0;
    position: fixed;
    background: rgba(0,0,0,0.5);
    width: 100%;
    height: 100%;
  }
  .modal h1 {
    color: #03cfb4;
    border: none;
    padding: 0;
  }
  .modal p {
    font-style: normal;
  }

  /* sale styles */
  .modal.sale {
    background: crimson;
    color: white;
  }
  .modal.sale h1 {
    color: white;
  }
</style>