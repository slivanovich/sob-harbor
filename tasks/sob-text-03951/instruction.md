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
SV St. Georg: SV St. Georg Hamburg is a German association football club playing in Hamburg.  The club was established 3 June 1895 and shares a common origin with "FC Hammonia Hamburg": both sides arose out of the students group Seminarvereinigung Frisch-Auf with "St. Georg" being formed first on the left bank of the Alster River, and "Hammonia" appearing later on the right bank.  Like their brother side, "St. Georg" was a founding member of the German Football Association (Deutscher Fussball Bund or German Football Association) at Leipzig in 1900.  However, while "Hammonia" folded after only a short existence, "St. Georg" still plays today.

Liberty Baptist Church (Grooverville, Georgia): Liberty Baptist Church is a historic church built about 1858 in Grooverville, Georgia.  It was added to the National Register of Historic Places on August 20, 2013.  It is located on Liberty Church Road.  There is a Georgia Historical Commission historical marker at the site.  According to the marker: "In 1841 the Ocklochnee anti-Missionary Baptist Association passed a ruling to dismiss members believing in the 'new fangled institutions of the day.'"  One of the excommunicated sisters joined with others in forming the Liberty Baptist Church.  The church includes a slave gallery.  Freed slaves from the area formed First Elizabeth Church in Grooverville.

Primary rock: Primary rock is an early term in geology that refers to crystalline rock formed first in geologic time, containing no organic remains, such as granite, gneiss and schist as well as igneous and magmatic formations from all ages.  Webster's Revised Unabridged Dictionary published in 1913 provides the following term as used in geology:

Japp–Maitland condensation: The Japp–Maitland condensation is an organic reaction and a type of Aldol reaction and a tandem reaction.  In a reaction between the ketone 2-pentanone and the aldehyde benzaldehyde catalyzed by base the bis Aldol adduct is formed first.  The second step is a ring-closing reaction when one hydroxyl group displaces the other in a nucleophilic substitution forming an oxo-tetrahydropyran.

Konstantin Vakulovsky: Captain Konstantin Konstantinovich Vakulovsky (born 28 October 1894, died Summer 1918) was a World War I flying ace credited with six aerial victories.  A major general's son, he volunteered for aviation duty on 8 August 1914, six days after graduating from university.  He taught himself to fly, and became one of Russia's first military pilots on 13 June 1915.  After escaping the fall of the Novogeorgievsk Fortress in a hazardous flight, Vakylovsky flew reconnaissance missions, some through heavy ground fire.  Given command of the newly formed First Fighter Detachment, he became a flying ace credited with six aerial victories.  He died in a flying accident during Summer 1918.

Temperate forest: Temperate forests correspond to forest concentration formed in the northern and southern hemisphere, or in temperate regions.  It is the same as a tropical forest except for the climate and some of the animals adaptations.  Main characteristics include: wide leaves, large and tall trees, large wild canopy and non seasonal vegetation.  Temperate forests can be further distinguished by weather patterns and geographical features that favor the predominance of certain kinds of trees.  In temperate coniferous forests, evergreen conifers predominate, while in temperate broadleaf and mixed forests, a more even distribution exists between evergreen trees and deciduous trees.  Temperate deciduous forests, a subgroup of temperate broadleaf forests, consist of trees that lose their leaves every year.  Finally, temperate rainforests typically have heavy rainfall and dense humidity.  But in some temperate forests there are just trees with needles and do not shed their leaves during the winter, so the climate is a little different and not as cold.  They are also known as montane forests.

Harris, Forbes &amp; Co.: Harris, Forbes & Co. was an investment banking affiliate of Harris Bank incorporated in 1911.  Harris, Forbes firm was acquired by Chase Manhattan Bank in 1930 to form Chase Harris, Forbes.  Just two years later, in 1932, the firm was dissolved after the passage of the Glass–Steagall Act in 1932.  Chase transferred what remained of its securities business to the Bank of Boston's newly formed First Boston Corporation, buttressing that firm's early municipal bond department.

Bauhaus (band): Bauhaus were an English post-punk band, formed in Northampton, England in 1978.  The group consisted of Peter Murphy (vocals, occasional instruments), Daniel Ash (guitar), Kevin Haskins (drums) and David J (bass).  The band was originally named Bauhaus 1919 in reference to the first operating year of the German art school Bauhaus, although they shortened the name within a year of formation.  One of the first gothic rock groups, Bauhaus were known for their dark image and gloomy sound, although they mixed many genres, including dub, glam rock, psychedelia and funk.

Forest for the Trees: Forest for the Trees was a group started by Carl Stephenson in 1993.  The project produced only a single full-length album during its duration.  Self-titled, the album was released in 1997 after being delayed by a nervous breakdown that kept Stephenson from working on it for several years.  Forest for the Trees produced only one single of note titled "Dream."  Forest for the Trees had many members, including John "coz" Acosta, Beck, Papa Bear Martinez, Mark Petersen, Don Device, David Strayer /drums, Chris Camacho/ bass and Jasper & Amadeus amongst others.  One album remains unreleased as of 2006 being shelved by the now non-existent DreamWorks Records.  In addition to be the creator of the group and producing, Stephenson plays violin, guitar, sitar, drums, keyboards and the didgeridoo.  "Forest for the Trees is also beautifully infected with a collage of sounds from answering machines to dripping water to roller coasters, which bring a real-life aspect to rather abstract music."  The band performed at the 2002 Coachella Music Festival.

West Bengal Legislative Assembly election, 1967: The West Bengal Legislative Assembly election, 1967 was held in Indian state of West Bengal in 1967 to elect 280 members to the West Bengal Legislative Assembly.  United Front led by Ajoy Mukherjee won majority of seats in the election, and formed first non-Congress government of the state.

Question: Which band was formed first, Forest for the Trees or Bauhaus?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_comparison": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "formation_year": {
            "type": "integer",
            "description": "The year the band was formed."
          }
        },
        "required": [
          "band_name",
          "formation_year"
        ],
        "additionalProperties": false
      },
      "description": "Details of the bands being compared."
    },
    "first_formed_band": {
      "type": "string",
      "description": "The name of the band that was formed first."
    },
    "first_formation_year": {
      "type": "integer",
      "description": "The year the first formed band was established."
    }
  },
  "required": [
    "band_comparison",
    "first_formed_band",
    "first_formation_year"
  ],
  "additionalProperties": false
}
