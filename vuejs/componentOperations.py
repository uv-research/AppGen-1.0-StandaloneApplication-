part1="""<template>
  <div class="hello">
    <h1>{{ msg }}</h1>"""
    
part2="""
    <button class="btn btn-primary" @click="onSubmit">submit</button><br/>
    <span v-if="result !== ''">
      <h3>The result is: {{result}}</h3>
    </span>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {"""
      
part3="""
      result: ''
    }
  },
  props: {
    msg: String
  },
  methods: {
    onSubmit: function () {"""

part4="""
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
</style>"""