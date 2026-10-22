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
Cyanometalate: Cyanometallates or cyanometalates are a class of coordination compounds, most often consisting only of cyanide ligands. Most are anions.  Cyanide is a highly basic and small ligand, hence it readily saturates the coordination sphere of metal ions.  The resulting cyanometallate anions are often used as ligands for building more complex structures called coordination polymers, the best known example of which is Prussian blue, a common dyestuff.

Johann Jacob Diesbach: Johann Jacob Diesbach (] ) was a Swiss pigment and dye producer known for first synthesizing a blue pigment known as Prussian blue (i.e. iron blue or Berlin blue).

Perls' Prussian blue: Prussian blue is a common stain used by pathologists to detect the presence of iron in biopsy specimens, such as deposits of storage ferritin in bone marrow biopsy samples.

Bluing (fabric): Bluing, laundry blue, dolly blue or washing blue is a household product used to improve the appearance of textiles, especially white fabrics.  Used during laundering, it adds a trace of blue dye (often synthetic ultramarine, sometimes Prussian blue) to the fabric.

Cobalt blue: Cobalt blue is a blue pigment made by sintering cobalt(II) oxide with alumina at 1200 °C.  Chemically, cobalt blue pigment is cobalt(II) oxide-aluminium oxide, or cobalt(II) aluminate, CoAlO.  Cobalt blue is lighter and less intense than the (iron-cyanide based) pigment Prussian blue.  It is extremely stable and has historically been used as a coloring agent in ceramics (especially Chinese porcelain), jewelry, and paint.  Transparent glasses are tinted with the silica-based cobalt pigment smalt.

Prussian blue (medical use): Prussian blue, also known as potassium ferric hexacyanoferrate, is used as a medication to treat thallium poisoning or radioactive cesium poisoning.  For thallium it may be used in addition to gastric lavage, activated charcoal, forced diuresis, and hemodialysis.  It is given by mouth or nasogastric tube.  Prussian blue is also used in the urine to test for G6PD deficiency.

Prussian blue: Prussian blue is a dark blue pigment with the idealized chemical formula Fe7(CN)18 .  To better understand the binding situation in this complex compound the formula can also be written as Fe4[Fe(CN)6]3 · "x"H2O .  Another name for the color is Berlin blue or, in painting, Parisian or Paris blue.  Turnbull's blue is the same substance, but is made from different reagents, and its slightly different color stems from different impurities.

Mrs. Stewart's Bluing: Mrs. Stewart's Bluing (MSB) is a brand of liquid fabric bluing agent which whitens fabrics with a proprietary blue dye, primarily made of a colloid of ferric ferrocyanide (blue iron salt, also referred to as "Prussian blue") and water.  Its only official use is for whitening fabrics.  However, there have been many reports of customers finding interesting new ways to use Mrs Stewart's Bluing; whitening hair, dyeing hair, dyeing pets, cleaning windows, adding to bird baths, marking ski hills, dyeing jeans blue, and many more.

Yonen Buzz: Yonen Buzz is an original German-language manga by Christina Plaka and the continuation of "Plastic Chew" (originally entitled "Prussian Blue", but changed in order to avoid association with the white nationalist band Prussian Blue).  While "Prussian Blue" was published in German by Carlsen Verlag, "Yonen Buzz" was released by TOKYOPOP Germany.  TOKYOPOP is releasing both titles in English in 2006.  The release schedule is rather slow, as the author is a full-time Japanology student.

Persian blue: Persian blue (not to be confused with Prussian blue) comes in three major tones: Persian blue proper—a bright medium blue; medium Persian blue (a medium slightly grayish blue that is slightly indigoish); and a kind of dark blue that is much closer to the web color indigo; this darker shade of "Persian blue" is referred to as Persian indigo, dark Persian blue, or regimental.

Question: What does Prussian blue and Bluing have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entities_compared": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The two entities being compared for commonalities."
    },
    "common_purpose": {
      "type": "string",
      "description": "The shared purpose or function between the entities."
    },
    "application_area": {
      "type": "string",
      "description": "The specific area or material where the common purpose is applied."
    },
    "prussian_blue_role_in_bluing": {
      "type": "string",
      "description": "Describes how Prussian blue is specifically related to bluing."
    }
  },
  "required": [
    "entities_compared",
    "common_purpose",
    "application_area",
    "prussian_blue_role_in_bluing"
  ],
  "additionalProperties": false
}
