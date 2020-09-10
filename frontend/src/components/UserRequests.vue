<template>
    <div class="row">
        <b-card
            v-for="user in apiResponse"
            :key="user.Email"
            :title="user.Email"
            tag="article"
            style="max-width: 20rem; max-height: 20rem;"
            class="mb-2 mr-2"
            >
            <b-card-text>
                Age: {{CheckResponseValue(user.Age)}}
                <br>
                Activity: {{CheckResponseValue(user.Activity)}}
            </b-card-text>

            <b-button type="submit" variant="primary" v-on:click="CreateUser(user, $event)">Create</b-button>
        </b-card>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "UserRequests",
  data(){
      return{
          apiResponse: null,
      }
  },
  methods:{
    async getAllrequests(){
        this.apiResponse = ""
        await axios.get('http://localhost:8000/allforms/').then(response =>{
            this.apiResponse = response.data
            console.log(this.apiResponse)
        })
    },
    async CreateUser(user, evt){
        console.log(user)
        const params = {
            email:user.Email
        }
        await axios.post('http://localhost:8000/allforms/', params).then(response =>{
            evt.target.innerText = "Created"
            evt.target.disabled = true
        })
        
    },
    CheckResponseValue(val){
        const ValuesDictionary = {
            "Age":{
                'T':'15-18', 
                'Y':'18-21',  
                'A':'21-40', 
                'MA':'40-60',  
                'O':'60+',
            },
            "Activities":{
                'L':'LOW', 
                'M':'MIDDLE', 
                'H':'HIGH',
            } 
        }
        if(ValuesDictionary.Age[val] != null){
           return ValuesDictionary.Age[val] 
        }
        return ValuesDictionary.Activities[val]
    }
  },
  mounted(){
      this.getAllrequests()
  }
};
</script>