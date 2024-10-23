using UnityEngine;

public class FollowTouch : MonoBehaviour
{
    // Speed at which the character moves towards the touch point
    public float moveSpeed = 5f;

    // Reference to the Rigidbody2D component
    private Rigidbody2D rb;

    // To track the target position
    private Vector2 targetPosition;

    // To check if we should move
    private bool isMoving = false;

    void Start()
    {
        // Get the Rigidbody2D component attached to the character
        rb = GetComponent<Rigidbody2D>();
        targetPosition = rb.position;  // Set the initial target to the character's current position
    }

    void Update()
    {
        // Check for touch input (for Android devices)
        if (Input.touchCount > 0)
        {
            Touch touch = Input.GetTouch(0);  // Get the first touch

            // Convert touch position to world position
            Vector3 touchWorldPos = Camera.main.ScreenToWorldPoint(touch.position);
            targetPosition = new Vector2(touchWorldPos.x, touchWorldPos.y);  // Update the target position

            // Start moving towards the target
            isMoving = true;
        }

        // Check for left mouse button click (for PC or testing in Unity Editor)
        if (Input.GetMouseButtonDown(0))
        {
            // Convert mouse position to world position
            Vector3 mouseWorldPos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
            targetPosition = new Vector2(mouseWorldPos.x, mouseWorldPos.y);  // Update the target position

            // Start moving towards the target
            isMoving = true;
        }

        // Move towards the target if needed
        if (isMoving)
        {
            // Move the character towards the target position smoothly
            Vector2 newPosition = Vector2.MoveTowards(rb.position, targetPosition, moveSpeed * Time.deltaTime);
            rb.MovePosition(newPosition);

            // Stop moving if the character has reached the target position
            if (Vector2.Distance(rb.position, targetPosition) < 0.1f)
            {
                isMoving = false;
            }
        }
    }
}
