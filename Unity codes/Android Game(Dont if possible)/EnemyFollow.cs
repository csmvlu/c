using UnityEngine;

public class EnemyFollow : MonoBehaviour
{
    public float enemySpeed = 3f;
    private Transform character;

    void Start()
    {
        character = GameObject.FindGameObjectWithTag("C").transform;
    }

    void Update()
    {
        transform.position = Vector2.MoveTowards(transform.position, character.position, enemySpeed * Time.deltaTime);
    }

    void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("C"))
        {
#if UNITY_EDITOR
            UnityEditor.EditorApplication.isPlaying = false;
#else
            Application.Quit();
#endif
        }
    }
}
