<template>
  <div class="container">
    <flash-message class="myCustomClass"></flash-message>
    <b-form @submit.prevent="test" @reset="onReset" class="mt-5">
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Age:" label-for="input-3">
        <b-form-select
          id="input-3"
          v-model="form.age"
          :options="Ages"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group id="input-group-3" label="Activity:" label-for="input-3">
        <b-form-select
          id="input-3"
          v-model="form.activity"
          :options="Activities"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-textarea
        id="textarea"
        v-model="form.description"
        placeholder="Additional information"
        rows="3"
        max-rows="6"
        :maxlength="max_length"
        v-on:input="description_length()"
        class="mt-5"
    ></b-form-textarea>
    <pre class="m-0" id="length">{{max_length}}</pre>
    <div class="mt-5">
      <b-button type="submit" variant="primary" class="mr-2">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </div>
    </b-form>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: "Form",
    data() {
      return {
        form: {
          email: '',
          age: null,
          activity: null,
          description: '',
          checked: []
        },
        Ages: [{ text: 'Select One', value: null }, 
                {text: '15-18', value: "T"}, 
                {text: '18-21', value: "Y"},  
                {text: '21-40', value: "A"}, 
                {text: '40-60', value: "MA"},  
                {text: '60+', value: "O"}],
        Activities: [{ text: 'Select One', value: null }, 
                      {text: 'LOW', value: "L"}, 
                      {text: 'MIDDLE', value: "M"}, 
                      {text: 'HIGH', value: "H"}],
        max_length: 500
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.age = null
        this.form.activity = null
        this.form.description = ''
        // Trick to reset/clear native browser form validation state
      },
      description_length(){
          document.querySelector("#length").innerHTML = this.max_length - this.form.description.length
      },
      async test(){
        const params = {
          Age : this.form.age,
          Activity : this.form.activity,
          Email : this.form.email,
          Additional : this.form.description
        }
        await axios.post("http://localhost:8000/ActivityForm/", params).then(response =>{
          if(response.status != 400){
            this.flashMessage.show({
                status: 'success',
                title: 'Success',
                message: "Your form has been created. Please wait for the response"
            });
          }
        }).catch(error => {
          if(error.response.data.Email){
            this.flashMessage.show({
                status: 'error',
                title: 'Error occured',
                message: error.response.data.Email[0]
            });
          }
        })
      }
    },
  }
</script>