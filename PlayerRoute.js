const Player = require('./models/Player')

const birthAttr = year => {
	if (year >= process.env.MINOR_BIRTH_YEAR) {
		return 'J'
	} else if (year < process.env.SENIOR_BIRTH_YEAR) {
		return 'S'
	}
	return ''
}

const genderAttr = gender => {
	return gender === 'FEMALE' ? 'W' : ''
}

module.exports = app => {

	app.route('/players')

		.get((reg, res) =>
			Player.find({ approved: true })
			.sort({ dwz: -1 })
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
}
