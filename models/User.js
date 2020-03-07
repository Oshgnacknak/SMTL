'use strict';

const mongoose = require('mongoose')
const { Schema } = mongoose

const { isEmail } = require('validator')

const UserSchema = new Schema({
	email: {
		type: String,
		required: true,
		validate: [ isEmail ]
	},
	encrypted_password: {
		type: String, 
		required: true 
	},
})

module.exports = mongoose.model('Users', UserSchema)
