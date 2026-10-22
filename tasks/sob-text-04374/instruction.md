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
Piotr Morawski: Piotr Morawski (December 27, 1976 – April 8, 2009) was a Polish mountaineer.  He was best known for making the first successful winter ascent together with Simone Moro of Shishapangma on January 14, 2005.  Morawski died aged 32 during an international Dhaulagiri/Manaslu expedition in Nepal.  He fell into a crevasse at an elevation of 5500 m while acclimatizing.

Annapurna Circuit: The Annapurna Circuit is a trek within the Annapurna mountain range of central Nepal.  The total length of the route varies between 160–230 km (100-145 mi), depending on where motor transportation is used and where the trek is ended.  The trek rises to an altitude of 5,416m on the Thorung La pass, touching the edge of the Tibetan plateau.  This trek crosses two different river valleys and encircles the Annapurna massif, crossing Thorung La (5416m/17769 ft), the highest pass on this trek.  Practically all trekkers hike the route anticlockwise, as this way the daily altitude gain is slower, and crossing the high Thorong La pass is easier and safer.  The mountain scenery, seen at close quarters includes the Annapurna Massif (Annapurna I-IV), Dhaulagiri, Machhapuchhre, Manaslu, Gangapurna, Tilicho Peak, Pisang Peak, and Paungda Danda.  Numerous other peaks of 6000-8000m in elevation rise from the Annapurna range.

Ghorepani: Ghorepani is a village in Myagdi District in the Dhaulagiri Zone of northern-central Nepal.  It lies 17 kilometres from the district capital of Beni at an elevation of approximately 2874 m (9429 ft).  The village lies within the Annapurna Conservation Area (ACA) and contains a number of "guest houses" that provide lodging and meals to mountain trekkers, many of whom spend the night before a pre-dawn trek to the top of nearby Poon Hill (3210m/10531 ft) to watch the sunrise.

Yutmaru Sar: Yutmaru Sar is a mountain in the Hispar mountain range, a subrange of the Karakoram.  At an elevation of 7283 m it is the 88th highest mountain in the world.  Yutmaru Sar is located in Gilgit-Baltistan, Pakistan.  It was first climbed in 1980.

TanDEM-X: TanDEM-X (TerraSAR-X add-on for Digital Elevation Measurement) is the name of TerraSAR-X's twin satellite, a German Earth observation satellite using SAR (Synthetic Aperture Radar) - a modern radar imaging technology.  Implemented in a Public-Private-Partnership between the German Aerospace centre (DLR) and EADS Astrium (now Airbus Defence and Space), it is a second, almost identical spacecraft to TerraSAR-X.  TanDEM-X is also the name of the satellite mission flying the two satellites in a closely controlled formation with typical distances between 250 and 500 m.  This unique twin satellite constellation will allow the generation of the WorldDEM™, the seamless global digital elevation models available from 2014.

Lupghar Sar: Lupghar Sar is 109th on the list of world tallest mountains.  It is located in Shishkat valley of Hunza Gojal.  It is part of the Momhail Sar cluster of mountains and has an elevation of 7200 m above sea level.  In Wakhi language Lupghar Sar translates as "the top of the big rock".

Malangutti Sar: Malangutti Sar is a mountain in the Karakoram mountains with a height of 7,207 metres (23,645 feet).  It is the 104th tallest mountain on Earth and located in Shimshal Valley.

Dhorpatan: Dhorpatan is a village in Nepal's Baglung District, 2,900 meters elevation in an east-west valley south of the Dhaulagiri mountain range in the Himalayas.  It is the headquarters of Dhorpatan Hunting Reserve.  There is a small community of indigenous Kham Magar people as well as Tibetan refugees.

Dhaulagiri: The Dhaulagiri massif in Nepal extends 120 km from the Kaligandaki River west to the Bheri.  This massif is bounded on the north and southwest by tributaries of the Bheri River and on the southeast by Myagdi Khola.  Dhaulagiri I is the seventh highest mountain in the world at 8167 m above sea level.  It was first climbed on May 13, 1960 by a Swiss/Austrian/Nepali expedition.

Systemic acquired resistance: The systemic acquired resistance (SAR) is a "whole-plant" resistance response that occurs following an earlier localized exposure to a pathogen.  SAR is analogous to the innate immune system found in animals, and there is evidence that SAR in plants and innate immunity in animals may be evolutionarily conserved.  Plants use pattern-recognition receptors to recognize conserved microbial signatures.  This recognition triggers an immune response.  The first plant receptors of conserved microbial signatures were identified in rice (XA21, 1995) and in Arabidopsis (FLS2, 2000).  Plants also carry immune receptors that recognize highly variable pathogen effectors.  These include the NBS-LRR class of proteins.  SAR is important for plants to resist disease, as well as to recover from disease once formed.  SAR can be induced by a wide range of pathogens, especially (but not only) those that cause tissue necrosis, and the resistance observed following induction of SAR is effective against a wide range of pathogens, which is why SAR resistance is sometimes called "broad spectrum."  SAR is associated with the induction of a wide range of genes (so called PR or "pathogenesis-related" genes), and the activation of SAR requires the accumulation of endogenous salicylic acid (SA).  The pathogen-induced SA signal activates a molecular signal transduction pathway that is identified by a gene called "NIM1", "NPR1" or "SAI1" (three names for the same gene) in the model genetic system "Arabidopsis thaliana".  SAR has been observed in a wide range of flowering plants, including dicotyledon and monocotyledon species.  SAR can be activated in corn, however, widely adapted commercial like Benzothiadiazole may not be efficient against "P. sorghi" causing common rust.

Question: What elevation does Malangutti Sar and Dhaulagiri have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mountains": {
      "type": "array",
      "description": "Details of the mountains being compared.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the mountain."
          },
          "elevation_meters": {
            "type": "integer",
            "description": "The elevation of the mountain in meters."
          }
        },
        "required": [
          "name",
          "elevation_meters"
        ],
        "additionalProperties": false
      }
    },
    "has_common_elevation": {
      "type": "boolean",
      "description": "Indicates whether Malangutti Sar and Dhaulagiri have any elevation in common."
    },
    "common_elevation_meters": {
      "type": "array",
      "description": "A list of elevations in meters that Malangutti Sar and Dhaulagiri have in common. This array will be empty if no common elevation is found.",
      "items": {
        "type": "integer"
      }
    }
  },
  "required": [
    "mountains",
    "has_common_elevation",
    "common_elevation_meters"
  ],
  "additionalProperties": false
}
