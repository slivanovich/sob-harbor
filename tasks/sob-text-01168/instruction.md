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
The Legend of Jimmy Blue Eyes: The Legend of Jimmy Blue Eyes is a 1964 short film directed by Robert Clouse.  Teddy Buckner composed the film score.  Janee Michelle had her film acting debut in the film.  John A. Alonzo, who would later become best known for his camerawork for "Chinatown", served as the cinematographer for "The Legend of Jimmy Blue Eyes".  The film was screened at the 1965 Cannes Film Festival.  Clouse won a Golden Globe Award for the film.  The film was nominated for the Academy Award for Best Live Action Short Film at the 37th Academy Awards, but lost to "".  "The Legend of Jimmy Blue Eyes" was Clouse's second film to be nominated for this award, the first being the 1962 film "The Cadillac".

Black lemur: The black lemur ("Eulemur macaco") is a species of lemur from the family Lemuridae.  Like all lemurs, it is endemic to Madagascar.  Originally, the species was thought to have two subspecies, "Eulemur macaco macaco" and "Eulemur macaco flavifrons", both of which were elevated to species status by Mittermeier "et al." in 2008 to "Eulemur macaco" and "Eulemur flavifrons" respectively.  The most startling difference between the two species is the eye colour; "Eulemur flavifrons", the blue-eyed black lemur, has blue eyes and is the only primate other than humans to have blue eyes, while "Eulemur macaco", the black lemur, has brown or orange eyes, and also has ear tufts.

Michael Smith (director): Michael I. Smith is an American television director and producer.  He is best known for his work on "", also working as a first assistant director and unit production manager on the series.  He also worked as a second assistant director on the films "Gloria" (1999), "Mickey Blue Eyes" (1999), "The Simian Line" (2000) and "Man on the Moon" (2001).  As well as the television series "The Sopranos" and "Hack".

Hugh Grant: Hugh John Mungo Grant (born 9 September 1960) is an English actor and film producer.  Grant has received a Golden Globe, a BAFTA, and an Honorary César for his work.  His films have earned more than US$2.4 billion from 25 theatrical releases worldwide.  Grant first received attention after earning the Volpi Cup for his performance in James Ivory's "Maurice" (1987) but achieved international success after appearing in the Richard Curtis-scripted "Four Weddings and a Funeral" (1994).  Grant used this breakthrough role as a frequent cinematic persona during the 1990s, delivering comic performances in films such as "Mickey Blue Eyes" (1999) and "Notting Hill" (1999).  One of the best known figures in 1990s British popular culture, Grant was in a high-profile relationship with Elizabeth Hurley, which was the focus of much attention in the British and international media.

Suite: Judy Blue Eyes: "Suite: Judy Blue Eyes" is a suite of short songs written by Stephen Stills and performed by Crosby, Stills & Nash (CSN).  It appeared on the group's self-titled debut album in 1969 and was released as a single, hitting #21 on the "Billboard" Hot 100 pop singles chart.  The song is ranked #418 on "Rolling Stone"′s list of the 500 Greatest Songs of All Time.  In Canada, "Suite: Judy Blue Eyes" peaked at number 11.

Michael Felgate: Michael Felgate (born 1 April 1991) is an English footballer who plays for Cypriot side Anagennisi Deryneia as a defender.

Mickey Blue Eyes: Mickey Blue Eyes is a 1999 an Anglo-American romantic comedy crime film directed by Kelly Makin.  Hugh Grant stars as Michael Felgate, an English auctioneer living in New York City who becomes entangled in his soon-to-be father-in-law's mafia connections.  Several of the minor roles are played by actors later featured in "The Sopranos".

Blue Eyes, Black Hair: Blue Eyes, Black Hair (French: Les Yeux bleus cheveux noirs ) is a 1986 novel by the French writer Marguerite Duras.  It tells the story of a couple who meet by chance in a small vacation town.  The man is homosexual and has recently fallen in love with a man with blue eyes and black hair.  After meeting the woman at a cafe, he pays the woman to come to his room so that he can look at her, presumably in order to learn something about women or love.

Lucky Chloe: Lucky Chloe (ラッキー・クロエ , Rakkī Kuroe ) , also known simply as Chloe, is a fictional character from the "Tekken" fighting game franchise by Bandai Namco Entertainment, making her debut in "Tekken 7".  She is a teenage girl wearing a black, pink and white kitten-themed costume, including cat ears, tail, and paws.  She is described as an otaku, having an obsession with Japanese pop culture and speaking in Japanese and English with a Japanese accent, though given her blonde hair and blue eyes, she may be of Caucasian descent.  She is hired by G Corporation to be a mascot commercial.  Her fighting style involves a lot of kicks, twirls, and flips, somewhat like a hip-hop dancer.  As shown in her, Eddy Gordo and Jack-7's own endings, she's a good actor in her idol persona, but is revealed to be a spoiled brat in real life.

Nemophila phacelioides: Nemophila phacelioides is a flowering forb native to Texas, Oklahoma, Louisiana, and Alabama.  The plant has medium-sized blue or purple flowers, and is an annual plant.  The flower is known commonly as baby blue eyes, Texas baby blue eyes, largeflower baby blue eyes, or flannel breeches.

Question: What nationality is Hugh Grant both in real life and as Michael Felgate in Mickey Blue Eyes?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film in which the character appears."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the actor and the character."
    },
    "nationality_applies_to": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "actor",
          "character"
        ]
      },
      "description": "Indicates whether the nationality applies to the actor, the character, or both."
    }
  },
  "required": [
    "actor_name",
    "character_name",
    "film_title",
    "nationality",
    "nationality_applies_to"
  ],
  "additionalProperties": false
}
