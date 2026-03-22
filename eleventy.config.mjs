import 'dotenv/config'

export default function (eleventyConfig) {
	eleventyConfig.addPassthroughCopy({ 'src/assets': 'assets' })

	eleventyConfig.addFilter('readableDate', (value) => {
		if (!value) return ''
		const d = value instanceof Date ? value : new Date(value)
		return new Intl.DateTimeFormat('en-GB', {
			year: 'numeric',
			month: 'short',
			day: '2-digit',
		}).format(d)
	})

	return {
		dir: {
			input: 'src',
			output: '_dist',
			includes: '_includes',
			layouts: '_includes/layouts',
			data: '_data',
		},
		markdownTemplateEngine: 'njk',
		htmlTemplateEngine: 'njk',
		templateFormats: ['njk', 'md', 'html'],
	}
}

