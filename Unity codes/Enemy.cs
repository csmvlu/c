using UnityEngine;

public class EnemyFollow : MonoBehaviour
{
    public Transform character;  // Reference to the character's transform
    public float enemySpeed = 3f; // Enemy speed, less than character speed

    void Start()
    {
        // Find the character by tag "C"
        GameObject characterObject = GameObject.FindGameObjectWithTag("C");
        if (characterObject != null)
        {
            character = characterObject.transform;
        }
        else
        {
            Debug.LogError("Character not found!");
        }
    }

    void Update()
    {
        if (character != null)
        {
            // Calculate direction to the character
            Vector2 direction = (character.position - transform.position).normalized;

            // Move the enemy towards the character
            transform.position = Vector2.MoveTowards(transform.position, character.position, enemySpeed * Time.deltaTime);
        }
    }
}
