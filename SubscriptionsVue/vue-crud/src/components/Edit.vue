// Not using Edit.vue
<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="name">Name</label>
                <input
                    type="text"
                    class="form-control"
                    id="name"
                    v-model="subscription.name"
                
                    name="name"
                    placeholder="Enter name"
                   >
               
            </div>
            <div class="form-group">
                <label for="currency">Currency</label>
                <select
                    name="currency"
                    class="form-control"
                   
                    id="currency"
                    v-model="subscription.currency"
                    >
                    <option value="EUR">EUR</option>
                    <option value="USD">USD</option>
                </select>
                
            </div>
            <div class="form-group">
                <label for="amount">Amount</label>
                <input
                    type="number"
                    name="amount"
                   
                    class="form-control"
                    id="amount"
                    v-model="subscription.amount"
                    placeholder="Enter amount"
                   >
                
            </div>
            <div class="form-group">
                <label for="description">Description</label>
                <textarea
                    name="description"
                    class="form-control"
                    id="description"
                   
                    v-model="subscription.description"
                    cols="30"
                    rows="2"
                    ></textarea>
                
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';

var config = {
    headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers':'*',
                'Access-Control-Allow-Methods':'*'
            }
};
export default {
    data() {
        return {
            subscription: {
                name: '',
                currency: '',
                amount: '',
                description: '',
            },
            submitted: false
        }
    },
    mounted() {
        console.log('.....'+ this.$route.params.id,config)
        axios.get('http://127.0.0.1:8000/api/subscriptions/'+this.$route.params.id,{headers: {'Access-Control-Allow-Origin': '*','Access-Control-Allow-Headers':'*',
                'Access-Control-Allow-Methods':'*'}})
            .then( response => {
                console.log('!!!!!!!')
                console.log(response.data)
                this.subscription = response.data
            });
    },
    methods: {
        update: function () {
            // this.$validator.validate().then(result => {
            //     this.submitted = true;
            //     if (!result) {
            //         return;
            //     }
                axios
                    .put(
                        'http://127.0.0.1:8000/api/subscriptions/' + this.subscription.id,
                        {headers: {'Access-Control-Allow-Origin': '*'}}
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            // });
        }
    },
}
</script>