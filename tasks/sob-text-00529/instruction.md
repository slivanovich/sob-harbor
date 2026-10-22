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
North Fork Bull Run River: The North Fork Bull Run River is a tributary, about 6 mi long, of the Bull Run River in the U.S. state of Oregon.  Part of the system that provides drinking water to the city of Portland, it flows generally south through a protected part of the Mount Hood National Forest in Multnomah County.  It joins the Bull Run River at Bull Run Reservoir 1.

Second Bull Run Union order of battle: The following Union Army units and commanders fought in the Second Battle of Bull Run of the American Civil War.  The Confederate order of battle is listed separately.  Order of battle compiled from the army organization during the battle, the casualty returns and the reports.

South Fork Bull Run River: The South Fork Bull Run River is a tributary, about 6 mi long, of the Bull Run River in the U.S. state of Oregon.  Part of the system that provides drinking water to the city of Portland, it flows generally west through a protected part of the Mount Hood National Forest in Clackamas County.  It joins the Bull Run River at Bull Run Reservoir 2, about 8 mi from the larger stream's confluence with the Sandy River.

USNS Bull Run (T-AO-156): The SS Bull Run was a type T2 tanker built at Sun Shipbuilding and Drydock Co. in Chester, PA as hull number 287 and USMC number 362 in 1943.  In 1956, the ship was acquired by the US Navy from the Maritime Administration, assigned to MSTS, and placed in-service as the USNS Bull Run (T-AO-156).  It left the navy in 1957, going back to the Maritime Administration.  In 1969, the stern of the Bull Run was attached to the bow of the Type C4 ship the Anchorage, and the completed ship then retained the name Anchorage.  The bow of the Bull Run was then scrapped.

Second Battle of Bull Run: The Second Battle of Bull Run or Battle of Second Manassas was fought August 28–30, 1862 in Prince William County, Virginia, as part of the American Civil War.  It was the culmination of the Northern Virginia Campaign waged by Confederate Gen. Robert E. Lee's Army of Northern Virginia against Union Maj. Gen. John Pope's Army of Virginia, and a battle of much larger scale and numbers than the First Battle of Bull Run (or "First Manassas") fought on July 21, 1861 on the same ground.

Irvin McDowell: Irvin McDowell (October 15, 1818 – May 4, 1885) was a career American army officer.  He is best known for his defeat in the First Battle of Bull Run, the first large-scale battle of the American Civil War.  In 1862, he was given command of the I Corps of the Army of the Potomac.  He fought unsuccessfully against Stonewall Jackson's troops during the Valley Campaign of 1862, and was blamed for contributing to the defeat of United States troops at the Second Battle of Bull Run in August.

Battle of Okinawa: The Battle of Okinawa (Japanese: 沖縄戦 , Hepburn: Okinawa-sen ) (Okinawan: 沖縄戦 , "Uchinaa ikusa " ), codenamed Operation Iceberg, was a major battle of the Pacific War fought on the island of Okinawa by United States Marine and Army forces against the Imperial Japanese Army and included the largest amphibious assault in the Pacific War during World War II, the April 1, 1945, invasion of Okinawa itself.  The 82-day battle lasted from April 1 until June 22, 1945.  After a long campaign of island hopping, the Allies were planning to use Okinawa, a large island only 340 mi away from mainland Japan, as a base for air operations for the planned invasion of the Japanese home islands.

Elias Wright: Elias Wright (June 22, 1830 – January 2, 1901) was an American Union brevet brigadier general during the period of the American Civil War.  He was commissioned as a second lieutenant on August 17, 1861 and was promoted to first lieutenant five months later.  He participated in the Peninsular Campaign and was captured at the Battle of Gaines's Mill.  He later fought at the Second Battle of Bull Run and Battle of South Mountain.  He was promoted to captain on December 13, 1863, led a company at the Battle of Chancellorsville, but he soon month later was appointed major of the 10th United States Colored Infantry.  He was soon promoted to lieutenant colonel and colonel.  He received his appointment as brevet brigadier general dated to January 15, 1865.

Manassas National Battlefield Park: Manassas National Battlefield Park, located north of Manassas, in Prince William County, Virginia, preserves the site of two major American Civil War battles: the First Battle of Bull Run on July 21, 1861, and the Second Battle of Bull Run which was fought between August 28 and August 30, 1862 (also known as the "First Battle of Manassas" and the "Second Battle of Manassas", respectively).  The peaceful Virginia countryside bore witness to clashes between the armies of the North (Union) and the South (Confederacy), and it was there that Confederate General Thomas J. Jackson acquired his nickname "Stonewall."

Battle of Chantilly: The Battle of Chantilly (or Ox Hill, the Confederate name) took place on September 1, 1862, in Fairfax County, Virginia, as the concluding battle of the Northern Virginia Campaign of the American Civil War.  Thomas J. "Stonewall" Jackson's corps of the Army of Northern Virginia attempted to cut off the line of retreat of the Union Army of Virginia following the Second Battle of Bull Run but was attacked by two Union divisions.  During the ensuing battle, Union division commanders Isaac Stevens and Philip Kearny were both killed but the Union attack halted Jackson's advance.

Question: What battle had the code name Operation Iceberg, Battle of Okinawa or Second Battle of Bull Run?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "battle_name": {
      "type": "string",
      "description": "The name of the battle."
    },
    "code_name": {
      "type": "string",
      "description": "The code name associated with the battle."
    },
    "is_correct_answer": {
      "type": "boolean",
      "description": "Indicates if this battle is the correct answer to the question."
    },
    "conflict": {
      "type": "string",
      "description": "The larger conflict or war this battle was a part of."
    },
    "campaign": {
      "type": "string",
      "description": "The specific campaign within the larger conflict."
    }
  },
  "required": [
    "battle_name",
    "code_name",
    "is_correct_answer",
    "conflict",
    "campaign"
  ],
  "additionalProperties": false
}
