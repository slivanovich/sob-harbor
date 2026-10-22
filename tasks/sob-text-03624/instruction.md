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
Josquin Des Pres (20th century musician): Josquin Des Pres (Born Josquin Turenne Des Pres) is a 20th-century French born American composer, bassist, author, producer, songwriter and most known for his contributions to music media books for Hal Leonard Corporation and Mel Bay instructional music books.  Josquin has written a vast library of compositions and music techniques on bass, music studies and various collections which are used by music teachers, private studies and in schools both nationally and internationally as a standard tool in the music industry.  Des Pres is also a collaborative writer with English lyricist, poet, and singer Bernie Taupin on several compositions.  Josquin Des Pres also writes musical scores and music trailers for more than 40 major TV networks and television shows including The Ellen DeGeneres Show, The Bachelor (U.S. TV series), American Idol, The Tyra Banks Show, George Lopez (TV series), Anderson Cooper, TMZ on TV, Extra (TV program), American Chopper, Pawn Stars, Deadliest Catch, CNN, NBC, HGTV, TBS (U.S. TV channel), Bravo (U.S. TV network), Food Network, Animal Planet, Discovery Channel, History (U.S. TV channel), Travel Channel, CBS Television Stations, Viacom, VH1, ABC, BET, KPBS (TV), TLC (TV network), and The CW Network.  His works are also known on MTV Networks Television Series Catfish, The Seven, When I Was Seventeen, MTV Cribs, Pimp My Ride, Teen Mom, True Life and 10 on Top.

La casa de al lado: La casa de al lado ("Behind Closed Doors") is an American Spanish-language telenovela produced by the United States-based television network Telemundo.  This mystery is a remake of the Chilean telenovela "La familia de al lado" produced by TVN in 2010-2011 and is being adapted by the author of the original, José Ignacio Valenzuela making a story longer with many differences from the original.

La Madame: La Madame is a 2013 Spanish-language series produced by RTI Producciones with collaboration of Sierralta Entertainment Group for Mexico-based television network Canal de las Estrellas and United States-based television network UniMás.  Alicia Machado stars as the protagonist.

Mingle Media TV Network: Mingle Media TV Network is a digital TV network offering scripted, unscripted, live and produced lifestyle, celebrity and entertainment programming seven days a week.  Founded on 8 February 2010, the network is a leading producer of independent filmmaker content in the web TV series.  Mingle Media TV Network publishes their content through its web syndication network, including iTunes, Blip.TV, YouTube, Facebook, Twitter, Blogs, DailyMotion, Roku, Boxee and via the Stickam.com mobile app.

¿Quién Eres Tú?: ¿Quién eres tú?  ('Infringement) (also known in developing as "La Otra Cara") is a 2012 Spanish-language telenovela produced by RTI Producciones and Televisa for Mexico-based television network Gala TV and United States-based television network UniMás (formally Telefutura).  It is a remake of "La Usurpadora".

Peter M. Lenkov: Peter M. Lenkov is a TV and film writer and producer as well as being an occasional writer of comic books.  Lenkov's notable work includes the TV series La Femme Nikita , "Hawaii Five-0", "24" and "" and films such as "R.I.P.D.", "Demolition Man" and "Son in Law".  In comics, he wrote "R.I.P.D." and "", for which he was nominated for the Bram Stoker Award for Best Illustrated Narrative.  In 2005, he was nominated for an Emmy Award for his work on the hit TV series "24".  In 2009, he wrote an episode of "" for which acclaimed actor Ed Asner was nominated for an Emmy for Guest Star.  In 2011, "Hawaii Five-0" was awarded Best New Drama at the People's Choice Awards.  Other awards include a CAPE Award for Best Drama for "Hawaii Five-0", A Media Access Award for his work on "CSI:NY" and a Huntington Disease Honor for an episode of "The District".

La Voz... México: La Voz... México (English: "The Voice... Mexico" ) is a reality show and singing competition based on the format of "The Voice" originated in the Netherlands and part of the international franchise "The Voice" created by television producer John de Mol.  Mexico is the first Spanish-speaking country to adapt this format and the first among 6 globally.  The show began its first season on September 11, 2011, under the production of Televisa executive producer Miguel Angel Fox.  The series' first episode scored a rating of 28.2/47.1, surpassing Spanish-language TV series La Academia rating of 9.6/17.  The second season began on September 9, 2012 as scheduled, though was slightly delayed before the airing of its final episode due to the death of judge Jenni Rivera, who died in a plane crash in Iturbide, Nuevo León on December 9, 2012, dedicating an entire episode as a tribute to the late singer.

La virgen de la calle: Virgen de la Calle ("Virgin of the Street") is a 2013 Spanish-language telenovela that was produced by RTI Producciones and Televisa for United States-based television network UniMás and Venezuela-based television network RCTV.  It is a remake of "Juana la virgen", a Venezuelan telenovela produced for RCTV.  María Gabriela de Faría and Juan Pablo Llano are the protagonists.

Vision TV Network: Vision TV Network is a TV network owned by Vision247 in the United Kingdom that allows access to a network of foreign TV channels from within the UK.  Viewers have to subscribe online in order to watch the pay TV channels on Vision TV Network, which are delivered to Roku, Samsung, IOS and Android Apps.  As an IPTV service, Vision TV Network also allows two-way interactivity to enable functionality such as voting, commerce and targeted advertising.  The service initially broadcast French, Greek, Polish and Turkish channels.

UniMás: UniMás (stylized as UniMÁS, and originally known as TeleFutura from its launch on January 14, 2002 until January 7, 2013) is an American Spanish language broadcast television network that is owned by Univision Communications.  The network's programming, which is aimed at Hispanic Americans in the 18-34 age range, includes telenovelas and other serialized drama series, sports, sitcoms, reruns of imported series previously aired on parent network Univision, reality and variety series, and theatrically released feature films (primarily consisting of Spanish-dubbed versions of American movie releases).

Question: What was the original name of the United States-based TV network that produced the TV series La Madame?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tv_network_name": {
      "type": "string",
      "description": "The current name of the television network."
    },
    "original_name": {
      "type": "string",
      "description": "The original name of the television network."
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country where the television network is based."
    },
    "series_associated": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of TV series produced for or by this network."
    }
  },
  "required": [
    "tv_network_name",
    "original_name",
    "country_of_origin",
    "series_associated"
  ],
  "additionalProperties": false
}
