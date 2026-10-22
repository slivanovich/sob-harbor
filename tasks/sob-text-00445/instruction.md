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
Tomoyo Oshima: Tomoyo Oshima (大島 ともよ , Ōshima Tomoyo , born 1949 Akita, Japan) is a Japanese film editor, known as editor of Nagisa Oshima's and Shuji Terayama's films in her young days.  She is the director of Tokyo Filmex, a film festival.

David Hewlett: David Ian Hewlett (born 18 April 1968) is an English-born Canadian actor, writer, director, and voice actor best known for his role as Dr. Rodney McKay on the Canadian-American science fiction TV shows "Stargate SG-1", "Stargate Atlantis" and "Stargate Universe".  Younger television viewers may know him best from his two 1993 guest appearances on "Shining Time Station", portraying nosy journalist Ted Typo.

Forbidden Colours: "Forbidden Colours" is a 1983 song by David Sylvian and Ryuichi Sakamoto.  The song is the vocal version of the theme from the Nagisa Oshima film "Merry Christmas, Mr. Lawrence" (in certain territories retitled "Furyo").  It appears on the film's soundtrack album and was released as a single on Virgin Records in 1983 (the second collaborative single release by Sylvian and Sakamoto, following 1982's "Bamboo Houses").

Nagisa Oshima: Nagisa Oshima (大島 渚 , Ōshima Nagisa , March 31, 1932 – January 15, 2013) was a Japanese film director and screenwriter.  His films include "In the Realm of the Senses" (1976), a sexually explicit film set in 1930's Japan, and "Merry Christmas, Mr. Lawrence" (1983), about Japanese WW2 prisoners of war.

Merry Christmas, Mr. Lawrence: Merry Christmas, Mr. Lawrence (Japanese: Senjō no Merī Kurisumasu (戦場のメリークリスマス , "Merry Christmas on the Battlefield") , also known in many European editions as Furyo (俘虜, Japanese for "prisoner of war"), is a 1983 British-Japanese drama film directed by Nagisa Oshima, produced by Jeremy Thomas and starring David Bowie, Tom Conti, Ryuichi Sakamoto, Takeshi Kitano and Jack Thompson.

Max, Mon Amour: Max, Mon Amour a.k.a. Max, My Love is a 1986 film directed by Nagisa Oshima, starring Charlotte Rampling, Anthony Higgins, Victoria Abril, Pierre Étaix and Milena Vukotic.  The screenplay was written by Oshima and Jean-Claude Carrière, and the film was produced by Serge Silberman.

Fumio Watanabe: Fumio Watanabe (渡辺文雄 , Watanabe Fumio , October 31, 1929 – August 4, 2004) was a Japanese actor most known for his work with Japanese New Wave director Nagisa Oshima.  He was born in Tokyo and graduated from the University of Tokyo before joining the Shōchiku studio in 1956.

The Seed and the Sower: The Seed and the Sower is a book by South African writer Laurens van der Post, consisting of three interrelated stories blended into a novel, first published in 1963.  The novel was filmed in 1983 as "Merry Christmas Mr. Lawrence", directed by Nagisa Oshima and starring David Bowie, Tom Conti, Ryuichi Sakamoto and Takeshi Kitano.

Kei Satō: Kei Satō (佐藤 慶 , Satō Kei ) was a Japanese character actor and narrator.  He was born in Aizu.  He is known for his work with Japanese New Wave director Nagisa Oshima, and for several films with Kaneto Shindo, such as "Onibaba" and "Kuroneko".  He won the best actor award from "Kinema Junpo" for the films "The Ceremony" and "Nihon no akuryō".  He also worked as a narrator for many documentaries, both on television and film.

Cruel Story of Youth: Cruel Story of Youth (青春残酷物語 , Seishun Zankoku Monogatari ) is a 1960 Japanese film directed by Nagisa Oshima, starring Yusuke Kawazu and Miyuki Kuwano as teenage delinquents and lovers.  It is Oshima's second feature film and is known for its elements of French "nouvelle vague".  The film won the 1960 Blue Ribbon Awards for Best Newcomer for Oshima.

Question: Are Nagisa Oshima and David Hewlett of the same nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "nationalities_are_same": {
      "type": "boolean"
    }
  },
  "required": [
    "person_1",
    "person_2",
    "nationalities_are_same"
  ],
  "additionalProperties": false
}
