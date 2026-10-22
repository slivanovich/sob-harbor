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
Ray Cooper: Raymond Thomas "Ray" Cooper (born 19 September 1947) is an English virtuoso percussionist.  He is a session and road-tour percussionist, and occasional actor, who has worked with several musically diverse bands and artists including George Harrison, Billy Joel, Rick Wakeman, Eric Clapton, Pink Floyd and Elton John.  Cooper absorbed the influence of rock drummers from the 1960s and 1970s such as Ginger Baker, Carmine Appice, and John Bonham.  Incorporation of unusual instruments (for rock drummers of the time) such as cowbells, glockenspiel, and tubular bells, along with several standard kit elements, helped create a highly varied setup.  Continually modified to this day, Cooper's percussion set offers an enormous array of percussion instruments for sonic diversity such as the tambourine, congas, crash cymbals, cowbells, roto toms, tubular bells, the gong, snare and timpani.  For two decades Cooper honed his technique; In the 1990s, he reinvented his style.  He is known for the 7-minute percussion and drum solos he performed during the years 1990–1991 for Eric Clapton and for the 7-minute percussion and drum solos during all the 1994 Face to Face Tours with Billy Joel, and Elton John, and the tours with the Elton John band during the years of 1994–1995.

Nicomachus: Nicomachus of Gerasa (Greek: Νικόμαχος ; c. 60 – c. 120 CE) was an important ancient mathematician best known for his works "Introduction to Arithmetic" and "Manual of Harmonics" in Greek.  He was born in Gerasa, in the Roman province of Syria (now Jerash, Jordan), and was strongly influenced by Aristotle.  He was a Neopythagorean, who wrote about the mystical properties of numbers.

John Sprinzel: John Sprinzel (born October 1930 in Berlin) is a German born British former auto racing driver.  He was renowned for competing in saloon and sports car racing and rallying.  Sprinzel finished third overall in the inaugural 1958 British Saloon Car Championship season driving for his own Team Speedwell in an Austin A35.  Navigated by future BMC and Ford Competitions Manager Stuart Turner, he won the British Rally Championship in 1959, driving an Austin-Healey Sprite and an Alfa Romeo Giulietta TI.  In International events during 1960, he won his class at the 12 Hours of Sebring race and scored 2nd place overall in both the Liège-Rome-Liège and RAC rallies.  These successes were all achieved in Austin-Healey Sebring Sprites, a car he was instrumental in developing.  He has published three volumes of memoirs: 'Sleepless Knights' (1962), 'Spritely Years' (1994) and 'Lucky John' (2013) and also a tuning manual for BMC cars 'Modified Motoring' (1959 and 1961).

Diego De La Hoya: Diego de la Hoya (born August 13, 1994 in Mexicali, Baja California, Mexico) is a Mexican professional boxer in the Super Bantamweight division.  De la Hoya has represented Mexico in international tournaments and is one of the top rated Super Bantamweights in the country.

Alphonse Favier: Pierre-Marie-Alphonse Favier-Duperron C.M.(Chinese: 樊國樑 Pinyin:"Fan Guoliang" Wade-Giles: "Fan Kouo-Léang") (born 22 September 1837 at Marsannay-la-Côte, France; died 4 April 1905 in Beijing) was the controversial Roman Catholic (Chinese: 天主教; Pinyin: Tianzhu jiao; Lord of Heaven Religion) Lazarite Vicar Apostolic of Northern Chi-Li (直隸北境) (later Chihli; now Hebei), China (now incorporating the Roman Catholic Archdiocese of Beijing) and titular bishop of Pentacomia from 13 April 1899 until his death in 1905.  During the Boxer Uprising of 1900, Favier was responsible for the defence and preservation of the Xishiku Cathedral (西什库天主堂), commonly referred to as the Beitang (北堂, the North Cathedral) in Beijing, and the protection of thousands of Chinese Roman Catholic Christians.  In the aftermath of the Boxer Uprising, Favier was accused of looting.

Bonosus (usurper): Bonosus (died 280) was a late 3rd-century Roman usurper.  He was born in Hispania (Roman Spain) to a British father and Gallic mother.  His father—a rhetorician and "teacher of letters"—died when Bonosus was still young but the boy's mother gave him a decent education.  He had a distinguished military career with an excellent service record.  He rose successively through the ranks and tribuneships but, while he was stationed in charge of the Rhenish fleet c. 281 , the Germans managed to set it on fire.  Fearful of the consequences, he proclaimed himself Roman emperor at Colonia Agrippina (Cologne) jointly with Proculus.  After a protracted struggle, he was defeated by Marcus Aurelius Probus and hanged himself rather than face capture.

Hassan Saada: Hassan Saada (born 2 January 1994) is a Moroccan boxer.  He was initially scheduled to compete in the men's light heavyweight competition at the 2016 Summer Olympics, but Saada was ejected from the competition after being arrested for sexual assault the day before the opening ceremony.  Saada was arrested and jailed during the Olympics in Rio de Janeiro after allegations of sexual assault and attempted rape were made against him by two Brazilian women who worked in the Olympic Village in Barra da Tijuca as waitresses, one day before he was due to fight at the Olympic Games.  Saada was stripped of his Olympic competitor status, and could face 6-10 years in prison if convicted.

Hazel Wright Organ: The Hazel Wright Organ located in the former Crystal Cathedral in Garden Grove, California – scheduled to be reconsecrated as the Roman Catholic "Christ Cathedral" in 2019 – is one of the world's largest pipe organs.  As of 2008, it had 270 ranks and 16,061 pipes, fully playable from two 5-manual consoles.

Charna Halpern: Charna Halpern (born 1952) is a co-founder of the ImprovOlympic, now known as iO.  She was born and raised in Rogers Park, Chicago on the north side of Chicago.  In 1984, with partner Del Close, she began teaching Harold to many students in the Chicago theater community.  She and Close co-authored the book "Truth in Comedy: The Manual of Improvisation" with editor Kim "Howard" Johnson in 1994.  She published "Group Improvisation" in 2003 and "Art by Committee" in 2006.

Manuel Roman: Manuel Roman is a Mexican professional boxer from Paramount.  As of early 2015 he had 17 wins, 3 losses, and 3 draws.  Roman currently fights in the super bantamweight division.  On September 13, 2014, Roman lost to Leo Santa Cruz in the WBC super bantamweight championship of the world by TKO in the second round.  He was scheduled to face Diego De La Hoya on February 27, 2015.

Question: Who is the boxer who was scheduled to face Manual Roman that was born in 1994? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "boxer_name": {
      "type": "string",
      "description": "The name of the boxer who meets the criteria."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the boxer."
    },
    "opponent_name": {
      "type": "string",
      "description": "The name of the opponent the boxer was scheduled to face."
    },
    "scheduled_fight_date": {
      "type": "string",
      "description": "The date the fight was scheduled."
    }
  },
  "required": [
    "boxer_name",
    "birth_year",
    "opponent_name",
    "scheduled_fight_date"
  ],
  "additionalProperties": false
}
