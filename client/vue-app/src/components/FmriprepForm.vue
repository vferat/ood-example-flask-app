<template>
  <div class="modal-backdrop" @click.self="closeModal">
    <div class="modal-main">
      <h1>fMRIPrep</h1>
      <form>
        <label>BIDS dir</label>
        <input type="text" required v-model="bidsDir"/>

        <label>Skip BIDS validation</label>
        <input type="checkbox" id="checkbox" v-model="skip_bids_validation" />

        <label>Output spaces</label>
        <select v-model="output_spaces" multiple>
        <option>MNI152NLin2009aAsym</option>
        <option>MNIInfant</option>
        <option>MNIPediatricAsym</option>
        </select>

        <label>Bold to t1w degrees of freedom (bold2t1w-dof)</label>
        <input type="radio" id="true" value=6 v-model="bold2t1w_dof" />
        <label for="one">6</label>
        <input type="radio" id="false" value=9 v-model="bold2t1w_dof" />
        <label for="two">9</label>
        <input type="radio" id="false" value=12 v-model="bold2t1w_dof" />
        <label for="two">12</label>

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
            bidsDir: '',
            job_id: '',
            skip_bids_validation: false,
            bold2t1w_dof: 6,
            output_spaces: []

        }
    },
    methods: {
      submit() {
          console.log('Submitting job');

          const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ "bidsDir": this.bidsDir })
          };

          fetch(apiEndpoint + 'submit', requestOptions)
              .then(response => response.json())
              .then(data => {
                  console.log(data.job_id);
                  this.job_id = data.job_id;
              })
              .catch(error => {
                  console.error('Error fetching data:', error);
              });
      },
      closeModal() {
        this.$emit('close');
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