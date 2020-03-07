const express = require('express')
const bodyParser = require('body-parser')
const mongoose = require('mongoose')
const morgan = require('morgan')
const favicon = require('serve-favicon')
const bcrypt = require('bcrypt')

const User = require('./models/User')

const PORT = 3000
const app = express()

mongoose.Promise = global.Promise
mongoose.connect(process.env.MONGO_URL, { useNewUrlParser: true })
	.then(() => {
		console.log('MongoDB Connected successfully...')
		return User.countDocuments({})
	})
	.then(count => {
		if (count === 0) {
			const password = Math.random().toString(36).substring(7)
			bcrypt.hash(password, 10)
			.then(hash => 
				new User({ email: 'user@example.com', encrypted_password: hash })
				.save())
			.then(user => 
				console.log(`No users found: Generated default user ${user.email}:${password} CHANGE ASAP!`)
			)
		}
	})
	.catch(err => console.log(err))

app.use(morgan('combined'))
app.use(express.static('public'))
app.use('/admin', require('./admin'))
app.use(favicon('public/vereinslogo1.gif'))
app.use(bodyParser.json())

require('./PlayerRoute')(app)

app.listen(PORT, () => {
	console.log('SMTL server started on: ' + PORT)
})
