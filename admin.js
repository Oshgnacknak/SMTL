const AdminBro = require('admin-bro')
const AdminBroExpress = require('admin-bro-expressjs')
const AdminBroMongoose = require('admin-bro-mongoose')
const bcrypt = require('bcrypt')

const Player = require('./models/Player')
const User = require('./models/User')

AdminBro.registerAdapter(AdminBroMongoose)
const adminBro = new AdminBro({
	resources: [
		{
			resource: Player,
			options: {
				properties: {
					created_at: { isVisible: { list: true, filter: true, show: true, edit: false } }
				}
			}
		},
		{
			resource: User,
			options: {
				properties: {
					encrypted_password: {
						isVisible: false,
					},
					password: {
						type: 'password',
						isVisible: {
							list: false, edit: true, filter: false, show: false,
						},
					},
				},
				actions: {
					new: {
						before: async (request) => {
							if(request.payload.password) {
								request.payload = {
									...request.payload,
									encrypted_password: await bcrypt.hash(request.payload.password, 10),
									password: undefined,
								}
							}
							return request
						},
					}
				}
			}
		}
	],
	rootPath: '/admin',
	branding: {
		logo: '/vereinslogo1.gif',
		companyName: 'SMTL Admin',
		softwareBrothers: false	 
	}
})

const { COOKIE_PASSWORD } = process.env
if (!COOKIE_PASSWORD) {
	throw new Error('process.env.COOKIE_PASSWORD must be set')
}
module.exports = AdminBroExpress.buildAuthenticatedRouter(adminBro, {
	authenticate: async (email, password) => {
		const user = await User.findOne({ email })
		if (user) {
			const match = await bcrypt.compare(password, user.encrypted_password)
			if (match) {
				return user
			}
		}
		return false
	},
	cookiePassword: COOKIE_PASSWORD
})
