from binaryninja_cortex.platforms import MCU

class Chip(MCU):
    NAME="STM32L0"
    ROM_OFF=0x08000000 
    RAM_OFF=0x20000000
    IRQ=MCU.IRQ+ [
        "NVIC_WWDG_IRQ",
        "NVIC_PVD_IRQ",
        "NVIC_RTC_IRQ",
        "NVIC_FLASH_IRQ",
        "NVIC_RCC_IRQ",
        "NVIC_EXTI0_1_IRQ",
        "NVIC_EXTI2_3_IRQ",
        "NVIC_EXTI4_15_IRQ",
        "NVIC_TSC_IRQ",
        "NVIC_DMA1_CHANNEL1_IRQ",
        "NVIC_DMA1_CHANNEL2_3_IRQ",
        "NVIC_DMA1_CHANNEL4_5_IRQ",
        "NVIC_ADC_COMP_IRQ",
        "NVIC_LPTIM1_IRQ",
        "NVIC_USART4_5_IRQ",
        "NVIC_TIM2_IRQ",
        "NVIC_TIM3_IRQ",
        "NVIC_TIM6_DAC_IRQ",
        "NVIC_TIM7_IRQ",
        "NVIC_RESERVED4_IRQ",
        "NVIC_TIM21_IRQ",
        "NVIC_I2C3_IRQ",
        "NVIC_TIM22_IRQ",
        "NVIC_I2C1_IRQ",
        "NVIC_I2C2_IRQ",
        "NVIC_SPI1_IRQ",
        "NVIC_SPI2_IRQ",
        "NVIC_USART1_IRQ",
        "NVIC_USART2_IRQ",
        "NVIC_LPUART1_AES_RNG_IRQ",
        "NVIC_LCD_IRQ",
        "NVIC_USB_IRQ",
        ]
