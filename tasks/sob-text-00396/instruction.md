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
Developmentalist configuration: The developmentalist configuration is an socio-anthropological term used in development studies to describe the nature of "development."  The term was coined by Jean-Pierre Olivier de Sardan and is used by post-development theorists, postcolonialists, critical theorists and others.  The term describes the paradigm of governments, NGOs, individuals and researchers who seek to progress the "development" of a country through cosmopolitan ideals which bring about social change.

Souyuan: Souyuan is the fifth album by Swedish Dark ambient project Atrium Carceri.  It was released on November 18, 2008 through Cold Meat Industry

Herbivore men: Herbivore men or grass-eater men (草食(系)男子 , Sōshoku(-kei) danshi ) is a term used in Japan to describe men who have no interest in getting married or finding a girlfriend.  The term herbivore men was also a term that is described as young men who had lost their "manliness".  The term was coined by the author Maki Fukasawa in an article published on 13 October 2006.

Dark ambient: Dark ambient (in the 1980s also referred to as ambient industrial or black ambient) is a genre of post-industrial music that features foreboding, ominous, or discordant overtones, some of which were heavily inspired by elements of ambient music.  The term was coined in the early 1990s by Roger Karmanik to describe the music of Raison d'être and is strongly associated with the Cold Meat Industry record label.

Secular inflation: Secular inflation is an economic term used to describe a prolonged period of gentle or mild price increases.  Secular, or chronic, inflation is basically creeping inflation that continues to persist over a long period of time.  Creeping inflation is a term used to describe a gradual rather than drastic increase in prices.  Although most commonly used to describe a mild inflation rate, secular inflation can be used to describe most inflation rates that are spread over long periods of time.  This type of inflation can be consistent (without many downward movements) or intermittent (occurring at regular intervals).

Filmfarsi: Filmfarsi (in Persian:فیلمفارسی) is a cinematic term used in Iranian cinema criticism.  It was coined by Iranian film critic, Houshang Kavoosi.  It was coined to describe low-quality films mostly copied from the Bollywood cinema and with poor plots, mostly arranged with dance and singing.

Ultra-large-scale systems: Ultra-large-scale system (ULSS) is a term used in fields including Computer Science, Software Engineering and Systems Engineering to refer to software intensive systems with unprecedented amounts of hardware, lines of source code, numbers of users, and volumes of data.  The scale of these systems gives rise to many problems: they will be developed and used by many stakeholders across multiple organizations, often with conflicting purposes and needs; they will be constructed from heterogeneous parts with complex dependencies and emergent properties; they will be continuously evolving; and software, hardware and human failures will be the norm, not the exception.  The term 'ultra-large-scale system' was introduced by Northrop and others to describe challenges facing the United States Department of Defense.  The term has subsequently been used to discuss challenges in many areas, including the computerization of financial markets.  The term 'ultra-large-scale system' (ULSS) is sometimes used interchangeably with the term 'large-scale complex IT system' (LSCITS).  These two terms were introduced at similar times to describe similar problems, the former being coined in the USA and the latter in the UK.

Internal colonialism: Internal colonialism is a notion of structural political and economic inequalities between regions within a nation state.  The term is used to describe the uneven effects of economic development on a regional basis, otherwise known as "uneven development", and to describe the exploitation of minority groups within a wider society.  This is held to be similar to the relationship between metropole and colony, in colonialism proper.  The term used to describe the distinct separation of the dominant core, from the periphery in an empire (Howe, 2002).  It was created to describe the "blurred" lines between geographically close locations that are clearly different in terms of culture (Howe, 2002, p. 18).  Some other factors that separate the core from the periphery are: language, religion, physical appearance, types and levels of technology, and sexual behaviour (Howe, 2002, p. 19).

Indo people: Indo is a term used to describe Eurasian people who were a migrant population that associated themselves with and experienced the colonial culture of the former Dutch East Indies, a Dutch colony in Southeast Asia that became Indonesia after World War II.  It was used to describe people acknowledged to be of mixed Dutch and Indonesian descent, or it was a term used in the Dutch East Indies to apply to Europeans who had partial Asian ancestry.  The European ancestry of these people was predominantly Dutch, and also Portuguese, British, French, Belgian, German, and others.

Homosexual transsexual: Homosexual transsexual, synonymous with androphilic transsexual, is a term used by various sexologists, psychologists, and psychiatrists to describe trans women who are exclusively attracted to men, and less often trans men who are attracted to women.  The term has become controversial.  The concept of taxonomically categorizing trans women by sexual orientation originated with Magnus Hirschfeld in 1923, and was further posited by Harry Benjamin in 1966 as a component of the Benjamin scale.  The specific term "homosexual transsexual" was coined by Kurt Freund in 1973, and used from 1982 onward by him and others, notably Ray Blanchard, as part of a two-type taxonomy of male-to-female transsexuality.  This taxonomy has subsequently evolved into, and is in the present day referred to, as Blanchard's transsexualism typology.

Question: Who coined the term used to describe the genre of Souyuan?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "term_coined": {
      "type": "string",
      "description": "The specific term that was coined."
    },
    "genre_of_album": {
      "type": "string",
      "description": "The genre of the album in question."
    },
    "coiner_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who coined the term."
        },
        "coining_period": {
          "type": "string",
          "description": "The period when the term was coined."
        }
      },
      "required": [
        "name",
        "coining_period"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "term_coined",
    "genre_of_album",
    "coiner_details"
  ],
  "additionalProperties": false
}
