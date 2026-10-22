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
Darshan Singh Bhuller: Darshan Singh Bhuller (born March 4th, 1961 in Singapore) is a British dancer, teacher, artistic director, filmmaker, and award-winning choreographer.  Considered "one of the brightest stars of his generation" and a "darkly powerful performer," Bhuller danced for London Contemporary Dance Theatre, Siobhan Davies Dance Company, and served as assistant director for Richard Alston Dance Company before revitalizing Phoenix Dance Theatre as its artistic director.

Alicia Markova: Dame Alicia Markova DBE (1 December 1910 – 2 December 2004) was an English ballerina and a choreographer, director and teacher of classical ballet.  Most noted for her career with Sergei Diaghilev's Ballets Russes and touring internationally, she was widely considered to be one of the greatest classical ballet dancers of the twentieth century.  She was the first British dancer to become the principal dancer of a ballet company and, with Dame Margot Fonteyn, is one of only two English dancers to be recognised as a prima ballerina assoluta.  Markova was a founder dancer of the Rambert Dance Company, The Royal Ballet and American Ballet Theatre, and was co-founder and director of the English National Ballet.

Colin Connor (dancer): Colin Connor (born June 18, 1954) is a Canadian–British dancer, choreographer, and educator, based in the United States.  With over forty commissions that span the worlds of contemporary dance, ballet and flamenco.  Works draws from a large range of influences – musical, literary, social, and scientific – all used to bring attention back to the communicative power of the human body.  He frequently, collaborates with artists of other disciplines, including composers, artists, and designers.  As a choreographer, teacher and dancer, Connor is currently influencing the next generation of contemporary dancers and dance makers.  Dancers who have trained with Connor have gone on to Mark Morris Dance Group, Scapino Ballet, Hubbard Street Dance, The Limon Dance Company and others.

Etta Murfitt: Etta Murfitt is a British dancer, choreographer and the associate director of the New Adventures educational strand.  She has worked for Matthew Bourne for over 20 years in a variety of different roles.  She teaches throughout the UK and abroad for dance companies and dance institutions, as well as being a freelance faculty member of the London Contemporary Dance School and Young Place.

Stepping Out (UK TV series): Stepping Out was a British competitive dancing talent show that aired on ITV from 31 August to 28 September 2013 and was hosted by Davina McCall.  The judging panel, referred to on the show as "the front row", was confirmed on 29 August 2013 and consists of Mel B, Jason Gardiner and Wayne Sleep.  Unlike other similar dance shows, the dancers were all couples in real life, not one celebrity plus one professional dancer.

Rupert Doone: Rupert Doone (born Ernest Reginald Wollfield 14 August 1903 – 4 March 1966) was a British dancer, choreographer, theatre director, and teacher in London.

Terence Lewis (choreographer): Terence Lewis (born 10 April 1975) is an Indian dancer and choreographer, specializing in contemporary dance.  He is known as a choreographer and judge in reality dance series. ." Dance India Dance Season 1, 2, 3" (2009–2012) He runs his 'Terence Lewis Contemporary Dance Company' in Mumbai, holds dance workshops both in India and abroad.  He has choreographed Bollywood films like, "Lagaan" (2001), "Jhankaar Beats" (2003) and "Naach" (2004), apart from musicals, stage shows, ads, music videos and national and international dance competitions , as well as starring in a music video for "DJ Hot Remix Vol.3" called Badan Pe Sitare (Remix of old song by Harry Anand) He was recently a judge of "Nach Baliye 5", along with actress Shilpa Shetty and film director Sajid Khan.  And currently seen judging Nach Baliye Shriman v/s Shrimati along with actress and "Nach Baliye 5" judge Shilpa Shetty and film director and choreographer Farah Khan.  Terence Lewis also got Staar Parivaar Award for Favourite Judge.  He also choreographed Disney India's first theatre production Beauty and the Beast.

Tamsier Joof Aviance: Tamsier Joof Aviance or "Tamsier Aviance" (né Tamsier Joof — 17 May 1973, former stage name: "Tam Jo") is a British dancer, choreographer, actor, model, entrepreneur and radio presenter from a Senegalese and Gambian background.  He took the name ""Aviance"" after joining the House of Aviance — one of the legendary vogue-ball houses in the United States.  As well as appearing in several musicals, and as stage backing dancer for Mary Kiani, Take That and Janet Jackson, he was also known within the London voguing scene during the 1990s and is among the original London vogue dancers of that era.

Lizzie Gough: Elizabeth Anne Gough (born 30 September 1984) is a British dancer, television judge, and dance presenter who came in third during the first series of "So You Think You Can Dance".  In 2010, she made her first appearance as a judge for the BBC / CBBC television series "Alesha's Street Dance Stars".  Gough trained in dance at Fitzell Roberts School of Dance in Southampton, and both dance and musical theatre at Laine Theatre Arts, a performing arts college in Epsom, Surrey.

Wayne Sleep: Wayne Philip Colin Sleep OBE (born 17 July 1948) is a British dancer, director, choreographer, actor and panellist.  He was a Principal Dancer with the Royal Ballet and has appeared as a Guest Artist with several other ballet companies.  He was a judge on the ITV entertainment series "Stepping Out".

Question: When was the British dancer, director and choreographer who was part of the judge of Stepping Out born 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person identified."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the person."
    },
    "roles": {
      "type": "array",
      "description": "A list of professional roles held by the person.",
      "items": {
        "type": "string"
      }
    },
    "show_judged": {
      "type": "string",
      "description": "The name of the TV show where the person was a judge."
    }
  },
  "required": [
    "person_name",
    "birth_date",
    "roles",
    "show_judged"
  ],
  "additionalProperties": false
}
