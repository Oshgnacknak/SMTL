'use strict';

const mongoose = require('mongoose')
const { Schema } = mongoose

const { isEmail } = require('validator')

const PlayerSchema = new Schema({
	name: {
		type: String,
		required: true
	},
	email: {
		type: String,
		required: true,
		validate: [ isEmail ]
	},
	birth_year: {
		type: Number,
		required: true,
		min: 1,
		max: 2020,
		validate: [ Number.isInteger ]
	},
	gender: {
		type: String,
		enum: [ 'MALE', 'FEMALE', 'OTHER' ],
		default: 'MALE'
	},
	club: {
		type: String,
		default: ''
	},
	dwz: {
		type: Number,
		min: 0,
		validate: [ Number.isInteger ],
		default: 0
	},
	approved: {
		type: Boolean,
        default: false
	},
	created_at: {
		type: Date, 
		default: Date.now()
	}
})

module.exports = mongoose.model('Players', PlayerSchema)
