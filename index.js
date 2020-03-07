const express = require('express')
const bodyParser = require('body-parser')
const mongoose = require('mongoose')
const morgan = require('morgan')
const favicon = require('serve-favicon')
const bcrypt = require('bcrypt')

const User = require('./models/User')
const Player = require('./models/Player')

const PORT = process.env.PORT || 3000
const MINOR_BIRTH_YEAR = process.env.MINOR_BIRTH_YEAR || 2002
const SENIOR_BIRTH_YEAR = process.env.SENIOR_BIRTH_YEAR || 1961
const MONGO_URL = process.env.MONGO_URL || 'mongodb://mongo/SMTL'
const app = express()

mongoose.Promise = global.Promise
mongoose.connect(MONGO_URL, { useNewUrlParser: true })
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

const birthAttr = year => {
	if (year >= MINOR_BIRTH_YEAR) {
		return 'J'
	} else if (year < SENIOR_BIRTH_YEAR) {
		return 'S'
	}
	return ''
}
const genderAttr = gender => {
	return gender === 'FEMALE' ? 'W' : ''
}
app.route('/players')
	.get((reg, res) =>
		Player.find({ approved: true })
		.then(players =>
			players.map(player => {
				const { name, birth_year, gender, club, dwz } = player;
				const attr = birthAttr(birth_year) + genderAttr(gender)
				return { name, club, dwz, attr }
			}))
		.then(data => res.json(data))
		.catch(err => console.log(err))
	)
	.post((req, res) => {
		const { name, email, birth_year, gender, club, dwz } = req.body;
		new Player({ name, email, birth_year, gender, club, dwz })
		.save()
		.then(() => res.json({}))
		.catch(err => res.status(400).send(err))
	})

app.listen(PORT, () => {
	console.log('SMTL server started on: ' + PORT)
})
