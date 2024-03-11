<template>
  <div class="modal-backdrop" @click.self="closeModal">
    <div class="modal-main">
      <h1>fMRIPrep</h1>
      <form>
        <div class="form-group">
          <label for="bidsDir">BIDS dir</label>
          <input type="text" id="bidsDir" required v-model="bidsDir"/>
        </div>
        <div class="form-group">
          <label for="checkbox">Skip BIDS validation</label>
          <input type="checkbox" id="checkbox" v-model="skip_bids_validation" />
        </div>
        <div class="form-group">
          <label for="outputSpaces">Output spaces</label>
          <select id="outputSpaces" v-model="output_spaces" multiple>
            <option>MNI152NLin2009aAsym</option>
            <option>MNIInfant</option>
            <option>MNIPediatricAsym</option>
          </select>
        </div>
        <div class="form-group">
          <label>Bold to t1w degrees of freedom (bold2t1w-dof)</label>
          <div>
            <input type="radio" id="dof6" value="6" v-model="bold2t1w_dof" />
            <label for="dof6">6</label>
            <input type="radio" id="dof9" value="9" v-model="bold2t1w_dof" />
            <label for="dof9">9</label>
            <input type="radio" id="dof12" value="12" v-model="bold2t1w_dof" />
            <label for="dof12">12</label>
          </div>
        </div>
        <div class="form-group">
          <button @click.prevent="submit">Run</button>
        </div>
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
          this.$emit('close');
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