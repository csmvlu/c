using UnityEngine;

public class CameraShake : MonoBehaviour
{
    public float shakeDuration = 0.5f, shakeMagnitude = 0.3f, dampingSpeed = 1.0f;
    Vector3 initialPosition;
    float shakeTime = 0f;

    void Start() => initialPosition = transform.localPosition;

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.S)) shakeTime = shakeDuration;

        if (shakeTime > 0)
        {
            transform.localPosition = initialPosition + Random.insideUnitSphere * shakeMagnitude;
            shakeTime -= Time.deltaTime * dampingSpeed;
        }
        else transform.localPosition = initialPosition;
    }
}
