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
Eva Turnová: Eva Turnová (born 1966) is a Czech singer, songwriter, bass guitarist, teacher, translator and actress.  Since 2001 she was a member of The Plastic People of the Universe.  She left the band in 2015.  Between 1995-2001 she was a member of DG 307.  Her first husband was Czech actor David Matásek (divorced five years after the wedding).  In 2008, she released first solo album called "Eturnity".

Toby Sheldon: Tobias "Toby" Sheldon (born Tobias Strebel; 1980 – August 21, 2015) was a German songwriter who became a television reality star noted for having paid extraordinary amounts for plastic surgery (he himself estimated the total cost at over $100,000) in order to resemble singer Justin Bieber.  He appeared on the television shows "Botched" on the E! network and "My Strange Addiction" on TLC.  Some experts argued that Sheldon's obsession was a case of body dysmorphia.  This topic was discussed in depth during his appearance alongside Justin Jedlica ("The Human Ken Doll") on the talk show "Bethenny".

Anzi Destruction: Anzi Destruction (born Antero Koskikallio; 1982) is a Finnish rock musician.  He is known for his energic and wild live shows including fire breathing.  He was the lead singer of (2003–2010).  Prior to joining Stereo Junks! , he played guitar in glam/punk band Plastic Tears in late nineties.  In 2001 he released two solo EPs "Shoot I" and "Shoot II".  In 2010 he joined The Salvation as its lead singer.  He's first full length solo album, "High Clash Motherf***er", was released in April 2011.  It was followed in 2015 by the album "Black Dog Bias".

Josef Janíček: Josef Janíček (born 28 December 1947 in Prague, Czechoslovakia, now Czech Republic) is a Czech rock keyboardist, singer, accordion and guitar player.  He was a former guitarist of The Primitives Group; from 1969 he played with The Plastic People of the Universe.  He was also a member of Milan Hlavsa's band called "Půlnoc".  Since 1990, he is a member of The Velvet Underground Revival Band.

Paper or Plastic (song): "Paper or Plastic" is a song recorded by American singer Brooke Candy.  It was written by Josh Cumbee, Shari Short, and Afshin Salmani, and produced by NONFICTION for Candy's unreleased album "Daddy Issues".  It was released as the fourth promotional single from the record.  In 2017, Candy left RCA to focus on releasing a second extended play (EP), and the release of "Daddy Issues" was canceled.

Beto Cuevas: Luis Alberto Cuevas Olmedo (born September 12, 1967), better known as Beto Cuevas, is a Chilean-Canadian singer, plastic artist, painter, and actor.  He is the lead singer for the Chilean band La Ley.  In 2008 he launched his solo career with the release of his album, “Miedo Escenico”.  In 2012 he released his second album called “Transformación”.

Ryohei Yamamoto: Ryohei Yamamoto (山本 領平 , Yamamoto Ryōhei ) , born December 30, 1974 in Kyoto) is a Japanese R&B singer, also known as just Ryohei.  He debuted as "山本領平" (written in kanji) under Warner Music Japan on 2003 with single "Almost There".  Prior to that, on November 2002, he was featured on a track "Why Not?"  by Fantastic Plastic Machine.  In 2006 he shortened his name to just "Ryohei" (written in Roman letters) and transferred to the label Rhythm Zone.  He is known for his collaborations with m-flo, being featured on tracks such as "Miss You" and "Summer Time Love".

Brooke Candy: Brooke Candy (born July 20, 1989) is an American rapper and singer.  She independently released videos for her songs "Das Me", "Everybody Does" and "I Wanna Fuck Right Now".  Candy signed with RCA in February 2014, releasing her debut EP "Opulence" on May 6, 2014 which features title track as lead and major label debut single.  Later she joined Columbia's UK roster.  She has since left Sony.  Candy's second EP is set to be released in the fall of 2017.

Joe Karafiát: Joe Karafiát (born 1957 in Prague) is a Czech singer and guitarist.  In 1980, he emigrated from Czechoslovakia to London and he left England after two years.  Settled in Canada, he played with various musicians and also recorded an album with another Czech musician Vratislav Brabenec.  After the Velvet Revolution, he returned to Prague, where became a member of Garage.  In 1997, he joined The Plastic People of the Universe.  In 2014, he released debut EP called "Zodiak", which was produced by Boris Carloff.  Same year, he guested on "Dva divoký koně" by Czech singer Dáša Vokatá.

Lou Deprijck: Lou Deprijck (] ) is a Belgian singer and music producer born in 1946 in Lessines, Wallonia.  He was a major figure in the Belgian pop scene of the 1970s and 1980s, with more than 20 million copies of his compositions sold worldwide.  He is best known for the Plastic Bertrand song "Ça plane pour moi".

Question: When was the singer of Paper or Plastic born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer_name": {
      "type": "string",
      "description": "The name of the singer who recorded the song."
    },
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "birth_date": {
      "type": "string",
      "description": "The full birth date of the singer."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the singer."
    }
  },
  "required": [
    "singer_name",
    "song_title",
    "birth_date",
    "birth_year"
  ],
  "additionalProperties": false
}
