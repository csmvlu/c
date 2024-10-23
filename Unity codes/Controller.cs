using UnityEngine;

public class MoveUpDown : MonoBehaviour
{
    public float speed = 5f;

    void Update()
    {
        float moveVertical = Input.GetAxis("Vertical") * speed * Time.deltaTime; // W/S for up/down
        float moveHorizontal = Input.GetAxis("Horizontal") * speed * Time.deltaTime; // A/D for left/right
        transform.position += new Vector3(moveHorizontal, moveVertical, 0);
    }
}
