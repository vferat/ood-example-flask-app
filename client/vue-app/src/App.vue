<script>

const apiEndpoint = '/api_v1/';

export default {
  name: 'App',
  data() {
    return {
      name: 'test'
    }
  },

  mounted() {
      this.fetchData();
  },

  methods: {
      fetchData() {
          console.log('fetching data');
          fetch(apiEndpoint + '/greeting')
              .then(response => response.json())
              .then(data => {
                  this.name = data.name;
              })
              .catch(error => {
                  console.error('Error fetching data:', error);
              });
      }
  }
}
</script>

<template>
 <h1> {{ name }} </h1>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
