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
Incantation (band): Incantation is an American death metal band that was formed by John McEntee and Paul Ledney in 1989.  They are one of the leaders in the New York City death metal scene along with fellow bands Suffocation, Mortician and Immolation, even though the band is currently located in Johnstown, Pennsylvania.  To date the band has released ten full-length records, two live records, four EPs, two singles, three splits, one DVD, and three demos.  Their most recent album "Profane Nexus" was released through Relapse Records in August 2017.  The band have maintained a significant cult following and underground popularity since the 90s, and are considered to be highly influential on a range of later death metal bands including Dead Congregation, Grave Miasma, and Portal, who are often described as 'cavernous death metal'.  Incantation's music frequently draws on anti-Christian, Satanic and occult themes, and the band is notable for mixing widely varied tempos into their music, often playing slow, down-tuned passages similar to those performed by death-doom bands like Autopsy.

Jawbox: Jawbox was an American alternative rock band from Washington, D.C., United States.  Its original members were J. Robbins (vocals, guitar), Kim Coletta (bass guitar) and Adam Wade (drums).  Bill Barbot (vocals, guitar) and Zach Barocas (drums) later joined the group, with Barocas replacing Wade.

Corey Taylor: Corey Todd Taylor (born December 8, 1973) is an American musician, singer, songwriter, actor, and author, best known as the lead singer and lyricist of the American heavy metal band Slipknot and the American alternative metal band Stone Sour.

I, Human: I, Human is the second full-length album by Singaporean death metal band, Deus Ex Machina, and the first to feature a permanent vocalist, giving it more uniformity in contrast to The War Inside, which had a different singer for each track.  Musically, it is an edgy mixture of Death Metal and Thrash Metal with Melodic death metal and Progressive Metal interjections, coupled with a diversified vocal approach.  The lyrical content of the album deals with the future: Cloning.  Specifically, questions regarding its use, legality, implications and the possibility of a world full of clones fighting to gain their own identity.  The concept is based on Isaac Asimov's novel I,Robot, but also is influenced by other science fiction works such as "Blade Runner", "The 6th Day", "A.I. Artificial Intelligence", and "Warhammer 40,000".  Each songs discusses the ethical issues pertaining to cloning, shifting from first person to second person to third person perspective.  The band further divulges the mind frame of an unnamed clone character as it gradually realizes it is a clone, upon awaking from what it thought was a dream.  In its desire to strive for acceptance as an equal, the band delves into its thoughts, fears and plans and invokes these emotions and transforms them into an aural assault with thought-provoking lyrics.

Supreme Misanthropy: Supreme Misanthropy is the first full-length album by Swedish Black Metal band Blodsrit.  The album was the first of the Blodsrit band, and featured more death metal type music, but due to the vocals it was and still is today by many of its fans called black metal.

Bother (song): "Bother" is the second single from the heavy metal band Stone Sour's self-titled debut album.  It was originally released as a solo song by frontman Corey Taylor, but the billing was later changed to Stone Sour.  The song was one of Stone Sour's first songs to put them into the mainstream.  The cover features Taylor's hands and rings, one of them being a Spider-Man ring which is a reference to the song being featured on the soundtrack to the film "Spider-Man" (although the track is credited to Taylor as the performer not Stone Sour) and to Taylor being a fan of Spider-Man.  The other has the number 8 on it, representing Taylor's number in Slipknot.  Taylor has stated that the song is about when he moved back to Des Moines from Denver, where he hoped to try to move forward with his music.

Death Breath: Death Breath is a Swedish death metal band, featuring Robert Pehrsson (Thunder Express/Dundertåget) and Nicke Andersson formerly of the death metal band Entombed, who wanted to return to playing drums and death metal.  The members of the band both have other bands but does not consider Death Breath to be a side project.  The band was formed in 2005 and was originally intended to be named Black Breath but to the band's surprise the name Death Breath had never been used by a metalband.  The band consider their music to be pure death metal, free from seven string guitars, five string basses and triggered drums.  The band's music is influenced by Slayer, Venom and Black Sabbath, Autopsy, Celtic Frost as well as old horror movies and HP Lovecraft.

Mortem: Mortem is a death metal band formed in 1986 in Lima, Peru.  They are the first Peruvian metal band to have toured Europe and the United States.  Mortem’s musical style is firmly rooted in the death metal, black metal and thrash metal of the nineteen-eighties.  Mortem's characteristic heavy sound is defined through slow and sinister death metal alternated with fast and aggressive counterparts.  Frantic tremolo picking in the style of early Possessed and Death built on passionate rhythmic percussion topped with wailing atonal and melodic guitar solos comprise a potent mix which lives up to the principle of death metal technique to craft pounding ritualistic and spirited death metal.  Vocals are forged from guttural rasps and often develop into high shrieks while lyrics deal mainly with the occult and anti-Christianity.

Swedish death metal: Swedish death metal is a death metal music scene developed in Sweden.  Many Swedish death metal bands are associated with the melodic death metal movement, thus giving Swedish death metal a different sound from other variations of death metal.  Unlike American death metal groups, the first Swedish bands were rooted in punk rock.  Although Norway is known for its quantity of black metal, Gothenburg in Sweden has a large melodic death metal scene, while Stockholm is known for its more raw death metal scene.

George Fisher (musician): George "Corpsegrinder" Fisher (born July 8, 1969) is an American extreme metal vocalist for the American death metal band Cannibal Corpse, the lesser-known melodic death metal band Paths of Possession, and the lesser-known extreme metal supergroup Serpentine Dominion.  He recorded two albums with Florida's Monstrosity before leaving and joining Cannibal Corpse in late 1995, replacing vocalist Chris Barnes, who is now the vocalist for Six Feet Under.  He also provided guest vocals for New York technical death metal band Suffocation on the songs "Reincremation" and "Mass Obliteration" from their debut album, "Effigy of the Forgotten", as well as guest vocals for California deathcore band Suicide Silence on the song "Control" from their fourth album, "You Can't Stop Me".  Fisher also performed guest vocals on Job for a Cowboy's 2014 album "Sun Eater" on the song "The Synthetic Sea."  As a death metal vocalist, Fisher employs the "death growl" extended vocal technique.

Question: Which person/band, Corey Taylor or Jawbox, is more affiliated with death metal type music?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_subject_1": {
      "type": "string",
      "description": "The name of the first person or band being compared."
    },
    "comparison_subject_1_genres": {
      "type": "array",
      "description": "A list of genres associated with the first subject.",
      "items": {
        "type": "string"
      }
    },
    "comparison_subject_2": {
      "type": "string",
      "description": "The name of the second person or band being compared."
    },
    "comparison_subject_2_genres": {
      "type": "array",
      "description": "A list of genres associated with the second subject.",
      "items": {
        "type": "string"
      }
    },
    "target_genre_type": {
      "type": "string",
      "description": "The specific genre type being used for comparison."
    },
    "more_affiliated_subject": {
      "type": "string",
      "description": "The person or band identified as more affiliated with the target genre type."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why one subject is more affiliated than the other based on the provided context."
    }
  },
  "required": [
    "comparison_subject_1",
    "comparison_subject_1_genres",
    "comparison_subject_2",
    "comparison_subject_2_genres",
    "target_genre_type",
    "more_affiliated_subject",
    "reasoning"
  ],
  "additionalProperties": false
}
