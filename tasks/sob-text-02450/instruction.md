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
Melanie Poole: Melanie (Mel) Poole is an Australian producer and writer.  She has run her own production company, called Production Hut, since 2006.  She is also the co-founder of a film production company called 18° Entertainment based in Queensland.

Pullip: Pullip (Korean: 풀잎 ) is a fashion doll created by Cheonsang Cheonha of South Korea in 2003.  Pullip has a jointed plastic body (1:6 scale) and a relatively oversized head (1:3 scale), with eyes that can move from side to side and eyelids that can blink.  Pullip was first marketed by Jun Planning out of Japan; but the company underwent management changes in early 2009 and, since then, has operated out of South Korea under the name Groove.  Since the release of the original female doll, other companion dolls have been added: male dolls Namu (나무, tree) and Taeyang (태양, sun); Taeyang's younger sister, Dal (달, moon); Dal's best friend, Byul (별, star); and Pullip's younger brother, Isul (이슬, dew).  In February 2013, a new member of the Pullip family was introduced, called Yeolume (열매, berry/fruit), who is Pullip's future daughter.  There is also a miniature line called Little Pullip, with 1:12 scale bodies and 1:6 scale heads.  Pullip and her counterpart dolls are often customized by collectors, with the most common customizations including wig changes, eye color changes, and rebodying.

In the Blink of an Eye (film): In the Blink of an Eye is a 2009 American film about the Rapture directed by Michael Sinclair.  It stars David A. R. White, Eric Roberts and Andrea Logan White, and was released to DVD on November 17, 2009.

Eye in the Sky (2007 film): Eye in the Sky () is a 2007 Hong Kong crime film starring Simon Yam, Tony Leung Ka-fai and Miss Hong Kong pageant winner Kate Tsui in her film debut.  Yam and Tsui play surveillance operatives on the trail of a gang of professional robbers led by Chan Chong-Shan (Leung).  The title is derived from the casino surveillance tech "eye in the sky".  It marks the directorial debut of Yau Nai-hoi, a long-time screenwriter for films directed by Johnnie To, who co-produced the film with his production company Milkyway Image.  "Eye in the Sky" premiered as an Official Selection at the 2007 Berlin International Film Festival, and as an Opening Film at the Hong Kong International Film Festival.  It was released in Hong Kong on 21 June 2007.

Blink (production company): Blink is a British production company and creative studio producing commercials, music videos, animations, art and fashion films.

David A. R. White: David Andrew Roy White (born May 12, 1970), also known as David A. R. White is an American actor, screenwriter and producer.  He is a co-founder of Pure Flix Entertainment, a distribution and production company specializing in Faith and Family-themed movies.

Flamsteed designation: A Flamsteed designation is a combination of a number and constellation name that uniquely identifies most naked eye stars in the modern constellations visible from southern England.

Indrajit Nattoji: Indrajit Nattoji (born 5 June 1971) is an Indian film director, screenwriter, producer, creative director, painter, designer and ad-filmmaker known for his works in Bollywood, television, and advertising.  Nattoji started his career in documentary film making and then moved from television to advertising to being a feature filmmaker.  He continues to be an ad-filmmaker and runs his own film production company, Blink Pictures.  Nattoji has made his directional debut Aagey Se Right (2009) which was produced by Ronnie Screwvala, under the banner of UTV Spotboy a subsidiary of UTV Motion Pictures.

Big Eye Records: Big Eye Music is a Los Angeles-based production company and independent record label founded in 2000.  Big Eye Music was the first label to focus exclusively on cover, karaoke and instrumental versions of songs from a wide variety of genres, including Rock, Hip Hop, Country and K-Pop.  The label also specializes in unique acoustic, symphonic, and lounge renditions of "Billboard" Hot 100 hits.  In addition, Big Eye Music has worked with artists such as Blackstreet, Salt-n-Pepa, Coolio, and others who have used Big Eye’s recordings as backing tracks for live performances as well as studio recordings.  The collective has also seen their work sampled by European DJs and electronic music producers.

List of brightest stars: This is a list of the brightest naked eye stars to +2.50 magnitude, as determined by their "maximum", "total" or "combined" apparent visual magnitudes as seen from Earth.  Although several of the brightest stars are also known close binary or multiple star systems, they do appear to the naked eye as single stars.  The given list below combines/adds the magnitudes of bright individual components.  Proper names in this list are those approved by the Working Group on Star Names

Question: In the Blink of an Eye stars the co-founder of what production company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film mentioned in the question."
    },
    "starring_actor": {
      "type": "string",
      "description": "The name of the actor who starred in the film."
    },
    "actor_role_in_company": {
      "type": "string",
      "description": "The role of the actor in the production company (e.g., co-founder)."
    },
    "production_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the production company."
        },
        "type": {
          "type": "string",
          "description": "A description of the company's specialization or type."
        }
      },
      "required": [
        "name",
        "type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "starring_actor",
    "actor_role_in_company",
    "production_company"
  ],
  "additionalProperties": false
}
