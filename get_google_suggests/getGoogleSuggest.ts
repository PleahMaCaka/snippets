import axios from "axios";

export async function getGoogleSuggest(query: string) {
	const res = await axios.get("https://suggestqueries.google.com/complete/search?output=toolbar&q=" + query)

	if (res.status != 200) return undefined
	else {
		return String(res.data)
			.replace("<?xml version=\"1.0\"?><", "")
			.replace("toplevel>", "")
			.replace("<\/toplevel>", "")
			.replace(/<CompleteSuggestion>/g, "")
			.replace(/<\/CompleteSuggestion>/g, "")
			.replace(/<suggestion /g, "")
			.replace(/ &#xB73B;/g, "")
			.replace(/\/>/g, " ")
			.replace(/data="/g, "|")
			.replace(/" /g, "")
			.slice(1).split("|")
	}
}
        
export {}
