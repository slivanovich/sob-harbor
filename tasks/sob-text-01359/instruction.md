Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Conrad Khunrath: Conrad Khunrath (1555, Leipzig -1613, probably in Hamburg) was a German merchant, alchemist, mint worker, doctor, author, editor, and translator.  He is particularly important as the author of "Medulla destillatoria", a work of Paracelsian iatrochemistry which was published in many editions for well over a century.

Bard (Dungeons &amp; Dragons): The bard is a standard playable character class in many editions of the "Dungeons & Dragons" fantasy role-playing game.  The bard class is versatile, capable of combat and of magic (Divine magic in earlier editions, arcane magic in later editions).  Bards use their artistic talents to induce magical effects.  The class is loosely based on the special magic that music holds in stories such as the Pied Piper of Hamelin, and in earlier versions was much more akin to being a Celtic Fili or a Norse Skald, although these elements have largely been removed in later editions.  Listed inspirations for bards include Taliesin, Homer, Will Scarlet and Alan-a-Dale.

Simon Sheppard (writer): Simon Sheppard is a writer of gay erotica and a sex-advice columnist from San Francisco.  He is the author of many books of gay sex writing, including "Man on Man: The Best of Simon Sheppard", "Sodomy!" , "Jockboys," "Kinkorama: Dispatches From the Front Lines of Perversion," "In Deep", and "Sex Parties 101".  He is also the editor of "Homosex: 60 Years of Gay Erotica," winner of the 2007 Lambda Literary Award for LGBT erotica; the anthology "Leathermen"; and is the coeditor of the anthologies "Rough Stuff" and "Roughed Up."  Sheppard's work is wide-ranging, often combining history, philosophy, and culture — high and low — with hardcore sex.  His first book, "Hotter Than Hell and Other Stories", won the Erotic Authors Association Award for Best Collection of the Year, and the title story of "In Deep" was shortlisted for the Rauxa Prize for Erotic Fiction.  His work has also appeared in over 300 anthologies and magazines, including many editions of "Best Gay Erotica" and "The Best American Erotica".  He wrote the syndicated column "Sex Talk," and the online columns "Perv" and "Notes of a Cranky Old Fag."  The online serial "The Dirty Boys' Club,” which he wrote for OutPersonals, was published as a novel in 2012.  He also curates and co-hosts, with Carol Queen, the San Francisco performance series Perverts Put Out!  Sheppard is openly gay, and is active in the queer artistic, political and AIDS-activist communities.  He lives with his husband in San Francisco, where "San Francisco" magazine dubbed him “our erotica king.”

Elle Girl: Elle Girl was the largest older-teen fashion and beauty magazine brand in the world with 12 editions and supplements worldwide.  Launched in August 2001, it was the younger sibling to "Elle" magazine, and similarly focused on beauty, health, entertainment and looked at daring fashion—its slogan: ""Dare to be different"".  The magazine was published monthly and was based in New York City.

Mission of Gravity: Mission of Gravity is a science fiction novel by Hal Clement.  The novel was serialized in "Astounding Science Fiction" magazine in April–July 1953.  Its first hardcover book publication was in 1954, and it was first published as a paperback book in 1958.  Along with the novel itself, many editions (and most recent editions) of the book also include "Whirligig World", an essay by Clement on creating the planet Mesklin that was first published in the June 1953 "Astounding".

Folio Society: The Folio Society is a privately owned London-based publisher, founded by Charles Ede in 1947 and incorporated in 1971.  It produces illustrated hardback editions of classic fiction and non-fiction books, poetry and children's titles.  Folio editions feature specially designed bindings and include artist-commissioned illustrations (most often in fiction titles) or researched artworks and photographs (in non-fiction titles).  Many editions come with their own slipcase.

Dictionnaire philosophique: The Dictionnaire philosophique (Philosophical Dictionary) is an encyclopedic dictionary published by Voltaire in 1764.  The alphabetically arranged articles often criticize the Roman Catholic Church and other institutions.  The first edition, released in June 1764, went by the name of "Dictionnaire philosophique portatif".  It was 344 pages and consisted of 73 articles.  Later versions were expanded into two volumes consisting of 120 articles.  The first editions were published anonymously in Geneva by Gabriel Grasset.  Due to the volatile content of the "Dictionnaire", Voltaire chose Grasset over his usual publisher to ensure his own anonymity.  There were many editions and reprints of the "Dictionnaire" during Voltaire's lifetime, but only four of them contained additions and modifications.  Furthermore, another work published in 1770, "Questions sur l'Encyclopédie", which contained reshaped and modified articles from the Encyclopédie always in alphabetical order, led many following editors to join this and the "Dictionnaire" (plus other minor works) in a unique opus.

Dak edition: Dak edition is the edition of a newspaper published earlier than other editions in order to be distributed to mofussil areas of India.  Shashi Tharoor provides his description of 1960s Dak edition as "yesterday's news with today's date on it.  Aggarwal states that it is the responsibility of the news editor to schedule the printing of the dak edition which he describes as meant for distant places as different from "city edition", which intended for the city in which it is printed.  Naqvi states that there are many editions of a paper such as dak edition, city edition and late city edition.  A dispatch appearing in "Allen's Indian mail" (1851) uses the term describing it as very different from the morning edition.

Sarra Manning: Sarra Manning is a writer from England.  She attended the University of Sussex and took up an English with Media Studies degree.  She became a freelance writer after submitting her work to "Melody Maker".  She worked as the entertainment editor for five years of the now-defunct teen magazine "J-17".  Manning was the editor of "Elle Girl" (UK edition), then re-launched "What To Wear" magazine for the BBC and has worked on UK magazines such as "Bliss" and "The Face".  She's contributed to "ELLE", "Seventeen", "The Guardian" and "Details" and is a contributing editor to "ELLE UK" and writes regularly for "Grazia", "Red" and "Stella", as well as consulting for a number of British magazine publishers.  She has been dubbed the "teen queen extraordinaire" following the release of her hit teen fiction book "Guitar Girl", and the popular "Diary of a Crush" trilogy.  Her first adult novel, "Unsticky" was published by Headline in 2009.  Her next teen novel, "Nobody's Girl" was published in 2010, and a second adult novel, "You Don't Have to Say You Love Me", was published in February 2011.  Her third adult novel, titled "Nine Uses for an Ex-Boyfriend", was published in February 2012.

George Gilfillan: George Gilfillan (30 January 1813 – 13 August 1878) was a Scottish author and poet.  One of the spasmodic poets, Gilfillan was also an editor and commentator, with memoirs, critical dissertations in many editions of earlier British poetry.

Question: How many editions did the magazine Sarra Manning was the editor of have?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the magazine Sarra Manning was the editor of."
    },
    "editor_name": {
      "type": "string",
      "description": "The name of the editor."
    },
    "number_of_editions": {
      "type": "integer",
      "description": "The total number of editions the magazine had worldwide."
    }
  },
  "required": [
    "magazine_name",
    "editor_name",
    "number_of_editions"
  ],
  "additionalProperties": false
}
